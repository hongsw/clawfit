"""
clawfit TUI — terminal questionnaire with live filtering.

Right panel starts with ALL tools visible, grouped by layer.
As questions are answered the panel re-scores and filters in real-time:
  • high-score tools float to the top with a bright score bar
  • low-score tools are dimmed
  • very low-score tools fade out completely

Keys: ↑/↓ move  Space/Enter select  ←/→ back/next  1-9 jump  q quit
"""

from __future__ import annotations

import curses
import json
import pathlib
import textwrap
from dataclasses import asdict
from typing import Any, Dict, List, Optional, Tuple

# ── colour pair ids ───────────────────────────────────────────
C_ACCENT   = 1   # bright purple text
C_SELECTED = 2   # white on purple (selected option)
C_SCORE_HI = 3   # high score — cyan bold
C_SCORE_MD = 4   # medium score — normal
C_DIM      = 5   # dim grey
C_HINT     = 6   # bottom hint bar (black on white)
C_DONE     = 7   # green completion
C_WARN     = 8   # amber next-step
C_LAYER    = 9   # layer header
C_BAR_HI   = 10  # score bar fill — high
C_BAR_LO   = 11  # score bar fill — low


def _init_colors() -> None:
    curses.start_color()
    curses.use_default_colors()
    bg = -1
    curses.init_pair(C_ACCENT,   curses.COLOR_MAGENTA, bg)
    curses.init_pair(C_SELECTED, curses.COLOR_WHITE,   curses.COLOR_MAGENTA)
    curses.init_pair(C_SCORE_HI, curses.COLOR_CYAN,    bg)
    curses.init_pair(C_SCORE_MD, curses.COLOR_WHITE,   bg)
    curses.init_pair(C_DIM,      curses.COLOR_WHITE,   bg)
    curses.init_pair(C_HINT,     curses.COLOR_BLACK,   curses.COLOR_WHITE)
    curses.init_pair(C_DONE,     curses.COLOR_GREEN,   bg)
    curses.init_pair(C_WARN,     curses.COLOR_YELLOW,  bg)
    curses.init_pair(C_LAYER,    curses.COLOR_MAGENTA, bg)
    curses.init_pair(C_BAR_HI,   curses.COLOR_CYAN,    bg)
    curses.init_pair(C_BAR_LO,   curses.COLOR_WHITE,   bg)


# ── data loading ──────────────────────────────────────────────

def _load_questions() -> List[Dict[str, Any]]:
    path = pathlib.Path(__file__).parent / "data" / "org_questions.json"
    return json.loads(path.read_text())["questions"]


def _load_all_tools() -> List[Dict[str, Any]]:
    path = pathlib.Path(__file__).parent / "data" / "tools_registry.json"
    return json.loads(path.read_text())


LAYER_LABELS = {
    "L1": "Base runtime",
    "L2": "Meta wrapper / harness",
    "L3": "Team harness / SSOT",
    "L4": "Memory / skills / tool-use",
    "L5": "Research / evaluation",
    "L6": "Data / knowledge infra",
    "L7": "Human interface",
}


def _layer_key(tool: Dict) -> str:
    lvl = tool.get("level", 1)
    # collapse 4a/4b/4c sub-levels into L4 for display
    if isinstance(lvl, str) and lvl.startswith("4"):
        return "L4"
    return f"L{lvl}"


def _score_tools(tools: List[Dict], answers: Dict[str, str]) -> List[Tuple[float, Dict]]:
    """Return (score, tool) pairs. Score 0.0 when no answers yet."""
    if not answers:
        return [(0.0, t) for t in tools]
    try:
        from .org_scorer import build_profile_from_answers, _score_tool
        profile = build_profile_from_answers(answers)
        return [(_score_tool(t, profile), t) for t in tools]
    except Exception:
        return [(0.0, t) for t in tools]


def _fetch_result_meta(answers: Dict[str, str]) -> Optional[Dict]:
    """Fetch stage/next-step metadata (lightweight, no full stack needed)."""
    if not answers:
        return None
    try:
        from .org_scorer import build_profile_from_answers, _maturity_label, _next_step_hint
        profile = build_profile_from_answers(answers)
        return {
            "maturity_stage": profile.maturity_stage,
            "maturity_label": _maturity_label(profile.maturity_stage),
            "next_step_hint": _next_step_hint(profile),
            "profile": profile,
        }
    except Exception:
        return None


# ── safe draw helpers ─────────────────────────────────────────

def _addstr(win, y: int, x: int, text: str, attr: int = 0) -> None:
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


def _score_bar(score: float, width: int) -> str:
    """Render a mini bar like [████░░░] for a 0-1 score."""
    inner = max(0, width - 2)
    filled = int(inner * score)
    return "[" + "█" * filled + "░" * (inner - filled) + "]"


# ── TUI application ───────────────────────────────────────────

class TUIApp:
    def __init__(self, stdscr):
        self.scr = stdscr
        self.questions = _load_questions()
        self.all_tools = _load_all_tools()
        self.answers: Dict[str, str] = {}
        self.current = 0
        self.cursor = 0
        self.scored: List[Tuple[float, Dict]] = [(0.0, t) for t in self.all_tools]
        self.meta: Optional[Dict] = None
        self.dirty = True

    def _recompute(self) -> None:
        """Recompute scores from confirmed answers."""
        self.scored = _score_tools(self.all_tools, self.answers)
        self.meta = _fetch_result_meta(self.answers)

    def _preview_answers(self) -> Dict[str, str]:
        """Confirmed answers + hovered (not yet confirmed) option."""
        q = self.questions[self.current]
        opts = q["options"]
        if 0 <= self.cursor < len(opts):
            return {**self.answers, q["id"]: opts[self.cursor]["value"]}
        return self.answers

    # ── layout ───────────────────────────────────────────────

    def _dims(self):
        h, w = self.scr.getmaxyx()
        left_w = max(28, min(42, w // 2))
        right_w = w - left_w - 1
        prog_h = 2
        hint_h = 1
        body_h = h - prog_h - hint_h
        return h, w, left_w, right_w, prog_h, hint_h, body_h

    # ── draw ─────────────────────────────────────────────────

    def draw(self) -> None:
        self.scr.erase()
        h, w, lw, rw, prog_h, hint_h, body_h = self._dims()
        q = self.questions[self.current]
        total = len(self.questions)
        n_answered = len(self.answers)

        # progress bar
        pct = n_answered / total
        bar_w = max(10, lw - 2)
        filled = int(bar_w * pct)
        bar = "█" * filled + "░" * (bar_w - filled)
        phase_tag = f"[{q['phase'].upper()}]"
        _addstr(self.scr, 0, 0,
                f" {bar} {self.current+1}/{total} {phase_tag}",
                curses.color_pair(C_ACCENT) | curses.A_BOLD)
        _hline(self.scr, 1, 0, curses.ACS_HLINE, w)

        # left panel
        lwin = self.scr.subwin(body_h, lw, prog_h, 0)
        self._draw_question(lwin, q)

        # vertical divider
        try:
            for row in range(prog_h, h - hint_h):
                self.scr.addch(row, lw, curses.ACS_VLINE)
        except curses.error:
            pass

        # right panel — use hover preview (confirmed answers + hovered option)
        if rw > 8:
            rwin = self.scr.subwin(body_h, rw, prog_h, lw + 1)
            preview = self._preview_answers()
            preview_scored = _score_tools(self.all_tools, preview)
            preview_meta = _fetch_result_meta(preview)
            self._draw_tools(rwin, n_answered, total, preview_scored, preview_meta)

        # hint bar
        is_last = self.current == total - 1
        q_answered = q["id"] in self.answers
        if is_last and q_answered:
            hint = "  Space/Enter/→  FINISH & EXIT   ← Back   q Quit  "
        elif is_last:
            hint = "  ↑/↓ Move   Space/Enter Select   ← Back   q Quit  "
        else:
            hint = "  ↑/↓ Move   Space/Enter Select+Next   ← Back   → Next   1-9 Jump   q Quit  "
        _addstr(self.scr, h - 1, 0, hint.ljust(w)[:w - 1],
                curses.color_pair(C_HINT))

        self.scr.refresh()
        self.dirty = False

    def _draw_question(self, win, q: Dict) -> None:
        h, w = win.getmaxyx()
        win.erase()

        lines = textwrap.wrap(q["text"], width=w - 2) or [q["text"]]
        row = 1
        for line in lines:
            _addstr(win, row, 1, line, curses.A_BOLD)
            row += 1
        row += 1

        opts = q["options"]
        chosen = self.answers.get(q["id"])
        for i, opt in enumerate(opts):
            if row >= h - 1:
                break
            is_sel = (i == self.cursor)
            is_ans = (opt["value"] == chosen)

            if is_sel and is_ans:
                marker, attr = "●", curses.color_pair(C_SELECTED) | curses.A_BOLD
            elif is_sel:
                marker, attr = "▶", curses.color_pair(C_ACCENT) | curses.A_BOLD
            elif is_ans:
                marker, attr = "●", curses.color_pair(C_ACCENT)
            else:
                marker, attr = "○", curses.A_DIM

            label_lines = textwrap.wrap(f" {marker} {opt['label']}", width=w - 3)
            for j, ll in enumerate(label_lines):
                if row >= h - 1:
                    break
                _addstr(win, row, 1, ("   " + ll.lstrip() if j > 0 else ll), attr)
                row += 1

        # previously answered chips at bottom
        answered_ids = [self.questions[i]["id"]
                        for i in range(self.current)
                        if self.questions[i]["id"] in self.answers]
        if answered_ids:
            sep_row = h - len(answered_ids[-5:]) - 2
            _addstr(win, max(row + 1, sep_row), 1, "─ answered ─", curses.A_DIM)
            for i, qid in enumerate(answered_ids[-5:]):
                idx = next(j for j, qq in enumerate(self.questions) if qq["id"] == qid)
                qq = self.questions[idx]
                val = self.answers[qid]
                opt_label = next((o["label"] for o in qq["options"] if o["value"] == val), val)
                r = max(row + 2, sep_row) + i + 1
                _addstr(win, r, 1,
                        f" {qq.get('short', qid)}: {opt_label}"[:w - 2],
                        curses.A_DIM)

    def _draw_tools(self, win, n_answered: int, total: int,
                    scored: List[Tuple[float, Dict]],
                    meta: Optional[Dict]) -> None:
        h, w = win.getmaxyx()
        win.erase()
        row = 0

        has_scores = bool(self.answers) or n_answered > 0

        # ── header ────────────────────────────────────────────
        if meta:
            stage_txt = f" Stage {meta['maturity_stage']} — {meta['maturity_label']}"
            _addstr(win, row, 0, stage_txt[:w - 1],
                    curses.color_pair(C_ACCENT) | curses.A_BOLD)
        else:
            _addstr(win, row, 0, " All tools — move cursor to preview",
                    curses.A_DIM)

        # tool count on right side of header
        visible_count = sum(1 for s, _ in scored if s >= (0.10 if n_answered >= 3 else 0))
        count_txt = f"{visible_count}/{len(scored)} "
        _addstr(win, row, max(0, w - len(count_txt) - 1), count_txt,
                curses.color_pair(C_DIM) | curses.A_DIM)
        row += 1

        if n_answered >= total:
            _addstr(win, row, 0, " ✓ Complete",
                    curses.color_pair(C_DONE))
            row += 1

        # ── score breakdown for #1 tool ───────────────────────
        # show only when we have scores and enough width
        top_scored = sorted(scored, key=lambda x: x[0], reverse=True)
        if has_scores and top_scored and top_scored[0][0] > 0 and w >= 36:
            top_score, top_tool = top_scored[0]
            profile = meta.get("profile") if meta else None
            if profile:
                try:
                    from .org_scorer import score_breakdown
                    bd = score_breakdown(top_tool, profile)
                    name = top_tool.get("name", "?")
                    _addstr(win, row, 0, f" ┌ {name[:w-5]} {int(top_score*100)}%",
                            curses.color_pair(C_SCORE_HI) | curses.A_BOLD)
                    row += 1
                    dims = [
                        ("task",    "Task "),
                        ("role",    "Role "),
                        ("maturity","Matur"),
                        ("network", "Net  "),
                        ("latency", "Lat  "),
                    ]
                    bar_w = max(4, w - 14)
                    for key, label in dims:
                        if row >= h - 1:
                            break
                        val = bd.get(key, 0)
                        filled = int(bar_w * val)
                        bar = "█" * filled + "░" * (bar_w - filled)
                        pct = int(val * 100)
                        attr = (curses.color_pair(C_SCORE_HI) | curses.A_BOLD if val >= 0.7
                                else curses.color_pair(C_SCORE_MD) if val >= 0.4
                                else curses.A_DIM)
                        _addstr(win, row, 1, f" {label} {bar} {pct:3d}%", attr)
                        row += 1
                    row += 1
                except Exception:
                    row += 1
            else:
                row += 1
        else:
            row += 1

        # ── group by layer ────────────────────────────────────
        layers_order = ["L1", "L2", "L3", "L4", "L5", "L6", "L7"]
        by_layer: Dict[str, List[Tuple[float, Dict]]] = {l: [] for l in layers_order}
        for score, tool in scored:
            lk = _layer_key(tool)
            if lk in by_layer:
                by_layer[lk].append((score, tool))

        # threshold: hide weak matches once enough answers given
        threshold = 0.10 if n_answered >= 3 else 0.0

        for lk in layers_order:
            items = by_layer[lk]
            if not items:
                continue
            if has_scores:
                items.sort(key=lambda x: x[0], reverse=True)
            visible = [(s, t) for s, t in items if s >= threshold]
            if not visible:
                continue
            if row >= h - 2:
                break

            # layer header with count
            label = LAYER_LABELS.get(lk, lk)
            n_vis = len(visible)
            n_tot = len(items)
            hdr = f" {lk} {label}"
            cnt = f" {n_vis}/{n_tot}"
            _addstr(win, row, 0, hdr[:w - len(cnt) - 1],
                    curses.color_pair(C_LAYER) | curses.A_BOLD)
            _addstr(win, row, max(0, w - len(cnt) - 1), cnt,
                    curses.A_DIM)
            row += 1

            # tier separators: ≥70% strong, 40-70% normal, <40% weak
            bar_w = max(4, min(8, w - 28))
            prev_tier = None
            for score, tool in visible:
                if row >= h - 1:
                    break
                name = tool.get("name", tool.get("id", "?"))

                if has_scores:
                    pct = int(score * 100)
                    tier = "strong" if score >= 0.70 else "mid" if score >= 0.40 else "weak"
                    # tier separator line
                    if prev_tier and tier != prev_tier and tier in ("mid", "weak"):
                        sep = "·" * min(w - 2, 20)
                        _addstr(win, row, 1, sep, curses.A_DIM)
                        row += 1
                        if row >= h - 1:
                            break
                    prev_tier = tier

                    bar = _score_bar(score, bar_w)
                    score_str = f"{pct:3d}%"
                    if tier == "strong":
                        attr = curses.color_pair(C_SCORE_HI) | curses.A_BOLD
                        bar_attr = curses.color_pair(C_BAR_HI) | curses.A_BOLD
                    elif tier == "mid":
                        attr = curses.color_pair(C_SCORE_MD)
                        bar_attr = curses.color_pair(C_BAR_LO)
                    else:
                        attr = curses.A_DIM
                        bar_attr = curses.A_DIM

                    col = 1
                    _addstr(win, row, col, score_str, attr)
                    col += 5
                    _addstr(win, row, col, bar, bar_attr)
                    col += len(bar) + 1
                    _addstr(win, row, col, name[:w - col - 1], attr)
                else:
                    _addstr(win, row, 2, f"• {name}"[:w - 3], curses.A_DIM)

                row += 1

            row += 1  # gap between layers

        # ── next step hint ────────────────────────────────────
        if meta and meta.get("next_step_hint") and row < h - 3:
            _addstr(win, row, 0, " ▶ NEXT STEP", curses.A_DIM | curses.A_BOLD)
            row += 1
            for line in textwrap.wrap(meta["next_step_hint"], width=w - 3)[:2]:
                if row >= h - 1:
                    break
                _addstr(win, row, 1, line, curses.color_pair(C_WARN))
                row += 1

    # ── input handling ────────────────────────────────────────

    def _select_current(self) -> None:
        q = self.questions[self.current]
        opts = q["options"]
        if 0 <= self.cursor < len(opts):
            self.answers[q["id"]] = opts[self.cursor]["value"]
            self._recompute()

    def _restore_cursor(self) -> None:
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
        self.scr.timeout(50)

        while True:
            if self.dirty:
                self.draw()

            key = self.scr.getch()
            if key == curses.ERR:
                continue

            q = self.questions[self.current]
            opts = q["options"]
            total = len(self.questions)

            if key in (ord('q'), ord('Q'), 27):
                return self._final_result()

            elif key == curses.KEY_RESIZE:
                self.scr.clear()
                self.dirty = True

            elif key in (curses.KEY_UP, ord('k')):
                self.cursor = (self.cursor - 1) % len(opts)
                self.dirty = True

            elif key in (curses.KEY_DOWN, ord('j')):
                self.cursor = (self.cursor + 1) % len(opts)
                self.dirty = True

            elif key in (ord(' '), ord('\n'), curses.KEY_ENTER, 10, 13):
                self._select_current()
                self.dirty = True
                if self.current < total - 1:
                    self.current += 1
                    self._restore_cursor()
                else:
                    if q["id"] in self.answers:
                        return self._final_result()

            elif key in (curses.KEY_LEFT, ord('h'), ord('b')):
                if self.current > 0:
                    self.current -= 1
                    self._restore_cursor()
                    self.dirty = True

            elif key in (curses.KEY_RIGHT, ord('l'), ord('\t'), 9):
                if q["id"] in self.answers:
                    if self.current < total - 1:
                        self.current += 1
                        self._restore_cursor()
                        self.dirty = True
                    else:
                        return self._final_result()

            elif ord('1') <= key <= ord('9'):
                idx = key - ord('1')
                if idx < total:
                    self.current = idx
                    self._restore_cursor()
                    self.dirty = True

        return self._final_result()

    def _final_result(self) -> Optional[Dict]:
        if not self.answers:
            return None
        try:
            from .org_scorer import build_profile_from_answers, org_recommend
            profile = build_profile_from_answers(self.answers)
            return asdict(org_recommend(profile))
        except Exception:
            return None


def run_tui() -> Optional[Dict]:
    """Launch TUI and return the final OrgRecommendation dict (or None)."""
    import os
    if not os.isatty(0):
        raise RuntimeError("TUI requires an interactive terminal.")
    return curses.wrapper(lambda scr: TUIApp(scr).run())
