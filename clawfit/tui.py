"""
clawfit TUI — terminal questionnaire with live results.

Layout:
  ┌─ progress ──────────────────────────────────┐
  │  question + options  │  live results panel  │
  │                      │                      │
  ├──────────────────────┴──────────────────────┤
  │  keybindings hint                           │
  └─────────────────────────────────────────────┘

Keys: ↑/↓ move  Space/Enter select  ←/→ back/next  q quit
"""

from __future__ import annotations

import curses
import json
import pathlib
import textwrap
from dataclasses import asdict
from typing import Any, Dict, List, Optional


# ── colour pair ids ──────────────────────────────────────────
C_NORMAL   = 0
C_HEADER   = 1   # purple on dark
C_SELECTED = 2   # white on purple
C_DIM      = 3   # grey
C_ACCENT   = 4   # bright purple text
C_PRIMARY  = 5   # layer primary badge
C_FUTURE   = 6   # layer future badge
C_SCORE    = 7   # score number
C_HINT     = 8   # bottom hint bar
C_DONE     = 9   # green done banner
C_WARN     = 10  # amber next-step


def _init_colors() -> None:
    curses.start_color()
    curses.use_default_colors()
    bg = -1  # transparent background

    curses.init_pair(C_HEADER,   curses.COLOR_MAGENTA, bg)
    curses.init_pair(C_SELECTED, curses.COLOR_WHITE,   curses.COLOR_MAGENTA)
    curses.init_pair(C_DIM,      curses.COLOR_WHITE,   bg)   # will use A_DIM
    curses.init_pair(C_ACCENT,   curses.COLOR_MAGENTA, bg)
    curses.init_pair(C_PRIMARY,  curses.COLOR_MAGENTA, bg)
    curses.init_pair(C_FUTURE,   curses.COLOR_WHITE,   bg)
    curses.init_pair(C_SCORE,    curses.COLOR_CYAN,    bg)
    curses.init_pair(C_HINT,     curses.COLOR_BLACK,   curses.COLOR_WHITE)
    curses.init_pair(C_DONE,     curses.COLOR_GREEN,   bg)
    curses.init_pair(C_WARN,     curses.COLOR_YELLOW,  bg)


def _load_questions() -> List[Dict[str, Any]]:
    path = pathlib.Path(__file__).parent / "data" / "org_questions.json"
    return json.loads(path.read_text())["questions"]


def _fetch_results(answers: Dict[str, str]) -> Optional[Dict[str, Any]]:
    if not answers:
        return None
    try:
        from .org_scorer import build_profile_from_answers, org_recommend
        profile = build_profile_from_answers(answers)
        return asdict(org_recommend(profile, top_per_layer=3))
    except Exception:
        return None


# ── safe addstr helpers ───────────────────────────────────────

def _addstr(win, y: int, x: int, text: str, attr: int = 0) -> None:
    """addstr that silently ignores out-of-bounds writes."""
    h, w = win.getmaxyx()
    if y < 0 or y >= h or x < 0 or x >= w:
        return
    max_len = w - x - 1
    if max_len <= 0:
        return
    try:
        win.addstr(y, x, text[:max_len], attr)
    except curses.error:
        pass


def _hline(win, y: int, x: int, ch: int, n: int) -> None:
    h, w = win.getmaxyx()
    if y < 0 or y >= h:
        return
    n = min(n, w - x - 1)
    if n <= 0:
        return
    try:
        win.hline(y, x, ch, n)
    except curses.error:
        pass


# ── TUI application ───────────────────────────────────────────

class TUIApp:
    def __init__(self, stdscr):
        self.scr = stdscr
        self.questions = _load_questions()
        self.answers: Dict[str, str] = {}
        self.current = 0          # question index
        self.cursor = 0           # option index within current question
        self.result: Optional[Dict] = None
        self.dirty = True         # needs redraw

    # ── layout ───────────────────────────────────────────────

    def _dims(self):
        h, w = self.scr.getmaxyx()
        left_w = max(30, min(44, w // 2))
        right_w = w - left_w - 1  # -1 for divider
        prog_h = 2
        hint_h = 1
        body_h = h - prog_h - hint_h
        return h, w, left_w, right_w, prog_h, hint_h, body_h

    # ── drawing ───────────────────────────────────────────────

    def draw(self) -> None:
        self.scr.erase()
        h, w, lw, rw, prog_h, hint_h, body_h = self._dims()
        q = self.questions[self.current]
        total = len(self.questions)

        # ── progress row ─────────────────────────────────────
        pct = self.current / total
        bar_w = max(10, lw - 2)
        filled = int(bar_w * pct)
        bar = "█" * filled + "░" * (bar_w - filled)
        phase_tag = f"[{q['phase'].upper()}]"
        _addstr(self.scr, 0, 0, f" {bar} {self.current+1}/{total} {phase_tag}",
                curses.color_pair(C_ACCENT) | curses.A_BOLD)

        # divider line between progress and body
        _hline(self.scr, 1, 0, curses.ACS_HLINE, w)

        # ── left panel: question ──────────────────────────────
        lwin = self.scr.subwin(body_h, lw, prog_h, 0)
        self._draw_question(lwin, q)

        # ── vertical divider ─────────────────────────────────
        try:
            for row in range(prog_h, h - hint_h):
                self.scr.addch(row, lw, curses.ACS_VLINE)
        except curses.error:
            pass

        # ── right panel: results ──────────────────────────────
        if rw > 5:
            rwin = self.scr.subwin(body_h, rw, prog_h, lw + 1)
            self._draw_results(rwin)

        # ── hint bar ─────────────────────────────────────────
        is_last = self.current == total - 1
        q_answered = self.questions[self.current]["id"] in self.answers
        if is_last and q_answered:
            hint = "  ↑/↓ Move   Space/Enter/→  FINISH & EXIT   ← Back   q Quit  "
        elif is_last:
            hint = "  ↑/↓ Move   Space/Enter Select (then → to Finish)   ← Back   q Quit  "
        else:
            hint = "  ↑/↓ Move   Space/Enter Select+Next   ← Back   → Next   q Quit  "
        _addstr(self.scr, h - 1, 0, hint.ljust(w)[:w - 1],
                curses.color_pair(C_HINT))

        self.scr.refresh()
        self.dirty = False

    def _draw_question(self, win, q: Dict) -> None:
        h, w = win.getmaxyx()
        win.erase()

        # question text (word-wrapped)
        lines = textwrap.wrap(q["text"], width=w - 2) or [q["text"]]
        row = 1
        for line in lines:
            _addstr(win, row, 1, line, curses.A_BOLD)
            row += 1
        row += 1  # blank line

        # answered chips above question (previous answers)
        # (shown as small inline breadcrumb at top)
        # options
        opts = q["options"]
        chosen = self.answers.get(q["id"])
        for i, opt in enumerate(opts):
            if row >= h - 1:
                break
            is_sel = (i == self.cursor)
            is_ans = (opt["value"] == chosen)

            if is_sel and is_ans:
                marker = "●"
                attr = curses.color_pair(C_SELECTED) | curses.A_BOLD
            elif is_sel:
                marker = "▶"
                attr = curses.color_pair(C_ACCENT) | curses.A_BOLD
            elif is_ans:
                marker = "●"
                attr = curses.color_pair(C_ACCENT)
            else:
                marker = "○"
                attr = curses.A_DIM

            label = f" {marker} {opt['label']}"
            label_lines = textwrap.wrap(label, width=w - 3)
            for j, ll in enumerate(label_lines):
                if row >= h - 1:
                    break
                prefix = "   " if j > 0 else ""
                _addstr(win, row, 1, (prefix + ll.lstrip() if j > 0 else ll), attr)
                row += 1
            row += 0  # no extra gap between options

        # previously answered summary at bottom
        answered_ids = [self.questions[i]["id"] for i in range(self.current)
                        if self.questions[i]["id"] in self.answers]
        if answered_ids:
            summary_row = h - len(answered_ids) - 2
            _addstr(win, max(row + 1, summary_row), 1, "─ answered ─",
                    curses.A_DIM)
            for i, qid in enumerate(answered_ids[-5:]):   # show last 5
                idx = next(j for j, qq in enumerate(self.questions) if qq["id"] == qid)
                qq = self.questions[idx]
                val = self.answers[qid]
                opt_label = next((o["label"] for o in qq["options"] if o["value"] == val), val)
                short = qq.get("short", qid)
                line = f" {short}: {opt_label}"
                r = max(row + 2, summary_row) + i + 1
                _addstr(win, r, 1, line[:w - 2], curses.A_DIM)

    def _draw_results(self, win) -> None:
        h, w = win.getmaxyx()
        win.erase()

        if not self.result:
            msg = "Answer a question to see live results"
            _addstr(win, h // 2, max(0, (w - len(msg)) // 2), msg, curses.A_DIM)
            return

        r = self.result
        row = 0

        # maturity header
        stage_line = f" Stage {r['maturity_stage']} — {r['maturity_label']}"
        _addstr(win, row, 0, stage_line[:w - 1],
                curses.color_pair(C_ACCENT) | curses.A_BOLD)
        row += 1

        total_q = len(self.questions)
        if len(self.answers) >= total_q:
            done = " ✓ Complete recommendation"
            _addstr(win, row, 0, done[:w - 1], curses.color_pair(C_DONE))
            row += 1
        row += 1  # blank

        # ── tool stack ───────────────────────────────────────
        stack = r.get("stack", [])
        if stack:
            _addstr(win, row, 0, " TOOL STACK", curses.A_DIM | curses.A_BOLD)
            row += 1

        for layer in stack:
            if row >= h - 1:
                break
            pri = layer["priority"]
            badge = f"[{pri.upper()[:3]}]"
            label = f"{layer['layer']} {layer['layer_label']}"
            badge_attr = (curses.color_pair(C_PRIMARY) | curses.A_BOLD
                          if pri == "primary"
                          else curses.color_pair(C_FUTURE) | curses.A_DIM)
            _addstr(win, row, 1, badge, badge_attr)
            _addstr(win, row, 7, label[:w - 9], curses.A_BOLD)
            row += 1

            for t in layer.get("tools", []):
                if row >= h - 1:
                    break
                score_str = f"{int(t['score']*100):3d}%"
                name = t["name"]
                line = f"  {score_str} {name}"
                _addstr(win, row, 1, line[:w - 2],
                        curses.color_pair(C_SCORE) if pri == "primary" else curses.A_DIM)
                row += 1
            row += 1  # gap between layers

        # ── core agent fit ───────────────────────────────────
        fits = [f for f in r.get("core_agent_fit", []) if f.get("fit_score", 0) > 0]
        if fits and row < h - 4:
            _addstr(win, row, 0, " CORE AGENT", curses.A_DIM | curses.A_BOLD)
            row += 1
            for fit in fits[:2]:
                if row >= h - 1:
                    break
                pct = int(fit["fit_score"] * 100)
                line = f"  {pct}% {fit['agent']} + {fit['llm']}"
                _addstr(win, row, 1, line[:w - 2], curses.color_pair(C_SCORE))
                row += 1
                if fit.get("maturity_note"):
                    note = f"     {fit['maturity_note']}"
                    _addstr(win, row, 1, note[:w - 2], curses.A_DIM)
                    row += 1
            row += 1

        # ── next step ────────────────────────────────────────
        hint = r.get("next_step_hint", "")
        if hint and row < h - 2:
            _addstr(win, row, 0, " NEXT STEP", curses.A_DIM | curses.A_BOLD)
            row += 1
            for line in textwrap.wrap(hint, width=w - 3):
                if row >= h - 1:
                    break
                _addstr(win, row, 1, line, curses.color_pair(C_WARN))
                row += 1

    # ── input handling ────────────────────────────────────────

    def _current_opts(self) -> List[Dict]:
        return self.questions[self.current]["options"]

    def _select_current(self) -> None:
        q = self.questions[self.current]
        opts = q["options"]
        if 0 <= self.cursor < len(opts):
            self.answers[q["id"]] = opts[self.cursor]["value"]
            self.result = _fetch_results(self.answers)

    def _restore_cursor(self) -> None:
        """Set cursor to current answer if any."""
        q = self.questions[self.current]
        val = self.answers.get(q["id"])
        if val:
            for i, opt in enumerate(q["options"]):
                if opt["value"] == val:
                    self.cursor = i
                    return
        self.cursor = 0

    def run(self) -> Optional[Dict]:
        _init_colors()
        curses.curs_set(0)
        self.scr.keypad(True)
        self.scr.timeout(50)   # ms — allows periodic redraw if needed

        while True:
            if self.dirty:
                self.draw()

            key = self.scr.getch()

            if key == curses.ERR:
                continue

            q = self.questions[self.current]
            opts = self._current_opts()
            total = len(self.questions)

            # ── quit ─────────────────────────────────────────
            if key in (ord('q'), ord('Q'), 27):  # q or ESC
                return self.result

            # ── resize ───────────────────────────────────────
            elif key == curses.KEY_RESIZE:
                self.scr.clear()
                self.dirty = True

            # ── move cursor ──────────────────────────────────
            elif key in (curses.KEY_UP, ord('k')):
                self.cursor = (self.cursor - 1) % len(opts)
                self.dirty = True

            elif key in (curses.KEY_DOWN, ord('j')):
                self.cursor = (self.cursor + 1) % len(opts)
                self.dirty = True

            # ── select option ────────────────────────────────
            elif key in (ord(' '), ord('\n'), curses.KEY_ENTER, 10, 13):
                self._select_current()
                self.dirty = True
                if self.current < total - 1:
                    # auto-advance to next question
                    self.current += 1
                    self._restore_cursor()
                else:
                    # last question: Enter again exits
                    if q["id"] in self.answers:
                        return self.result

            # ── back ─────────────────────────────────────────
            elif key in (curses.KEY_LEFT, ord('h'), ord('b')):
                if self.current > 0:
                    self.current -= 1
                    self._restore_cursor()
                    self.dirty = True

            # ── next / finish ─────────────────────────────────
            elif key in (curses.KEY_RIGHT, ord('l'), ord('\t'), 9):
                if q["id"] in self.answers:
                    if self.current < total - 1:
                        self.current += 1
                        self._restore_cursor()
                        self.dirty = True
                    else:
                        # last question answered → finish
                        return self.result

            # ── jump to question by number (1-9) ─────────────
            elif ord('1') <= key <= ord('9'):
                idx = key - ord('1')
                if idx < total:
                    self.current = idx
                    self._restore_cursor()
                    self.dirty = True

        return self.result


def run_tui() -> Optional[Dict]:
    """Launch TUI and return the final OrgRecommendation dict (or None)."""
    import os
    # Ensure we have a real terminal
    if not os.isatty(0):
        raise RuntimeError("TUI requires an interactive terminal.")
    return curses.wrapper(lambda scr: TUIApp(scr).run())
