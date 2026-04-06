"""
clawfit web UI server.

Serves a single-page questionnaire with live results.
Usage: clawfit serve [--port 7771] [--no-browser]
"""

from __future__ import annotations

import json
import pathlib
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from dataclasses import asdict

_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>clawfit — Org-Fit Diagnosis</title>
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    background: #0f1117;
    color: #e2e8f0;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
  }
  header {
    background: #1a1d2e;
    border-bottom: 1px solid #2d3148;
    padding: 14px 24px;
    display: flex;
    align-items: center;
    gap: 12px;
  }
  header h1 { font-size: 1.1rem; font-weight: 700; color: #a78bfa; }
  header span { font-size: 0.8rem; color: #64748b; }
  .main {
    display: flex;
    flex: 1;
    gap: 0;
    overflow: hidden;
  }

  /* ── Left panel: questionnaire ── */
  .left {
    width: 420px;
    min-width: 320px;
    background: #141624;
    border-right: 1px solid #2d3148;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }
  .progress-bar {
    height: 3px;
    background: #1e2035;
    position: relative;
  }
  .progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #7c3aed, #a78bfa);
    transition: width 0.4s ease;
  }
  .q-header {
    padding: 16px 20px 8px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 0.75rem;
    color: #64748b;
  }
  .q-phase {
    background: #1e2035;
    color: #818cf8;
    padding: 2px 8px;
    border-radius: 999px;
    font-weight: 600;
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
  .q-body {
    flex: 1;
    padding: 12px 20px 20px;
    overflow-y: auto;
  }
  .q-text {
    font-size: 1rem;
    font-weight: 600;
    color: #e2e8f0;
    margin-bottom: 18px;
    line-height: 1.5;
  }
  .options { display: flex; flex-direction: column; gap: 8px; }
  .option {
    background: #1a1d2e;
    border: 1.5px solid #2d3148;
    border-radius: 10px;
    padding: 12px 14px;
    cursor: pointer;
    transition: all 0.15s;
    font-size: 0.88rem;
    color: #cbd5e1;
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .option:hover { border-color: #7c3aed; color: #e2e8f0; background: #1e1f35; }
  .option.selected {
    border-color: #7c3aed;
    background: #1e1a35;
    color: #c4b5fd;
  }
  .option .dot {
    width: 16px; height: 16px;
    border-radius: 50%;
    border: 2px solid #4b5563;
    flex-shrink: 0;
    display: flex; align-items: center; justify-content: center;
  }
  .option.selected .dot {
    border-color: #7c3aed;
    background: #7c3aed;
  }
  .option.selected .dot::after {
    content: '';
    width: 6px; height: 6px;
    background: white;
    border-radius: 50%;
  }
  .nav {
    padding: 16px 20px;
    display: flex;
    gap: 10px;
    border-top: 1px solid #1e2035;
  }
  button {
    border: none; cursor: pointer;
    border-radius: 8px;
    font-size: 0.85rem;
    font-weight: 600;
    transition: all 0.15s;
    padding: 9px 18px;
  }
  .btn-prev {
    background: #1a1d2e;
    color: #94a3b8;
    border: 1.5px solid #2d3148;
    flex: 0 0 auto;
  }
  .btn-prev:hover:not(:disabled) { border-color: #7c3aed; color: #c4b5fd; }
  .btn-prev:disabled { opacity: 0.35; cursor: default; }
  .btn-next {
    background: #7c3aed;
    color: white;
    flex: 1;
  }
  .btn-next:hover:not(:disabled) { background: #6d28d9; }
  .btn-next:disabled { opacity: 0.45; cursor: default; }

  /* answered chips */
  .answered-list {
    padding: 8px 20px 4px;
    display: flex;
    flex-wrap: wrap;
    gap: 5px;
    min-height: 36px;
  }
  .chip {
    background: #1e2035;
    border: 1px solid #2d3148;
    border-radius: 6px;
    padding: 2px 8px;
    font-size: 0.7rem;
    color: #818cf8;
    cursor: pointer;
    display: flex; align-items: center; gap: 4px;
    transition: border-color 0.15s;
  }
  .chip:hover { border-color: #7c3aed; }
  .chip-label { color: #64748b; }

  /* ── Right panel: results ── */
  .right {
    flex: 1;
    overflow-y: auto;
    padding: 24px;
    background: #0f1117;
  }
  .placeholder {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
    color: #374151;
    gap: 12px;
    text-align: center;
  }
  .placeholder svg { opacity: 0.3; }
  .placeholder p { font-size: 0.9rem; }

  .result-header {
    display: flex; align-items: baseline; gap: 12px;
    margin-bottom: 20px;
  }
  .result-header h2 { font-size: 1.1rem; color: #a78bfa; }
  .maturity-badge {
    background: #1e1a35;
    border: 1px solid #7c3aed;
    border-radius: 999px;
    padding: 2px 10px;
    font-size: 0.72rem;
    color: #c4b5fd;
  }

  .section-title {
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #64748b;
    margin: 20px 0 10px;
  }

  .layer-card {
    background: #141624;
    border: 1px solid #2d3148;
    border-radius: 12px;
    padding: 14px 16px;
    margin-bottom: 10px;
  }
  .layer-card.primary { border-left: 3px solid #7c3aed; }
  .layer-card.future  { border-left: 3px solid #374151; opacity: 0.8; }
  .layer-top {
    display: flex; align-items: center; gap: 8px;
    margin-bottom: 6px;
  }
  .layer-badge {
    font-size: 0.65rem; font-weight: 700;
    padding: 1px 6px; border-radius: 4px;
    text-transform: uppercase;
  }
  .layer-badge.primary { background: #2e1b6b; color: #a78bfa; }
  .layer-badge.future  { background: #1e2035; color: #64748b; }
  .layer-name { font-weight: 600; font-size: 0.88rem; color: #e2e8f0; }
  .layer-why { font-size: 0.76rem; color: #64748b; margin-bottom: 10px; line-height: 1.4; }
  .tool-row {
    display: flex; align-items: center; gap: 8px;
    padding: 5px 0;
    border-top: 1px solid #1e2035;
  }
  .tool-score {
    font-size: 0.7rem;
    color: #818cf8;
    font-weight: 700;
    width: 32px; text-align: right; flex-shrink: 0;
  }
  .tool-name {
    font-size: 0.82rem;
    color: #cbd5e1;
    flex: 1;
  }
  .tool-link {
    font-size: 0.7rem;
    color: #4b5563;
    text-decoration: none;
    transition: color 0.15s;
  }
  .tool-link:hover { color: #a78bfa; }

  .agent-card {
    background: #141624;
    border: 1px solid #2d3148;
    border-radius: 10px;
    padding: 14px 16px;
    margin-bottom: 8px;
  }
  .agent-top {
    display: flex; align-items: center; gap: 8px; margin-bottom: 6px;
  }
  .agent-name { font-weight: 600; font-size: 0.9rem; color: #e2e8f0; }
  .score-pill {
    margin-left: auto;
    background: #1e1a35;
    border-radius: 999px;
    padding: 1px 8px;
    font-size: 0.72rem;
    font-weight: 700;
    color: #a78bfa;
  }
  .agent-note { font-size: 0.76rem; color: #818cf8; margin-bottom: 6px; }
  .agent-why { font-size: 0.75rem; color: #64748b; line-height: 1.5; }

  .next-step {
    background: #141624;
    border: 1px solid #2d3148;
    border-left: 3px solid #f59e0b;
    border-radius: 10px;
    padding: 14px 16px;
    font-size: 0.83rem;
    color: #94a3b8;
    line-height: 1.6;
    margin-top: 4px;
  }

  .spinner {
    display: inline-block;
    width: 16px; height: 16px;
    border: 2px solid #2d3148;
    border-top-color: #7c3aed;
    border-radius: 50%;
    animation: spin 0.7s linear infinite;
  }
  @keyframes spin { to { transform: rotate(360deg); } }

  .done-banner {
    background: #0d2a1a;
    border: 1px solid #166534;
    border-radius: 10px;
    padding: 10px 16px;
    font-size: 0.82rem;
    color: #4ade80;
    margin-bottom: 16px;
    display: flex; align-items: center; gap: 8px;
  }
</style>
</head>
<body>
<header>
  <h1>⚡ clawfit</h1>
  <span>Org-Fit Diagnosis — answer questions to find your tool stack</span>
</header>
<div class="main">

  <!-- Left: questionnaire -->
  <div class="left">
    <div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div>
    <div class="q-header">
      <span id="qCounter"></span>
      <span class="q-phase" id="qPhase"></span>
    </div>
    <div class="answered-list" id="answeredList"></div>
    <div class="q-body">
      <div class="q-text" id="qText"></div>
      <div class="options" id="optionsList"></div>
    </div>
    <div class="nav">
      <button class="btn-prev" id="btnPrev" onclick="nav(-1)" disabled>← Back</button>
      <button class="btn-next" id="btnNext" onclick="nav(1)" disabled>Next →</button>
    </div>
  </div>

  <!-- Right: live results -->
  <div class="right" id="resultsPanel">
    <div class="placeholder">
      <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2"/>
        <rect x="9" y="3" width="6" height="4" rx="1"/>
        <path d="M9 12h6M9 16h4"/>
      </svg>
      <p>Answer the first question<br>to see live recommendations</p>
    </div>
  </div>

</div>

<script>
let questions = [];
let answers = {};    // {question_id: option_value}
let current = 0;
let loading = false;

async function init() {
  const resp = await fetch('/api/questions');
  questions = await resp.json();
  renderQ();
}

function renderQ() {
  const q = questions[current];
  const total = questions.length;

  document.getElementById('progressFill').style.width = `${(current / total) * 100}%`;
  document.getElementById('qCounter').textContent = `${current + 1} / ${total}`;
  document.getElementById('qPhase').textContent = q.phase;
  document.getElementById('qText').textContent = q.text;

  // options
  const list = document.getElementById('optionsList');
  list.innerHTML = '';
  for (const opt of q.options) {
    const div = document.createElement('div');
    div.className = 'option' + (answers[q.id] === opt.value ? ' selected' : '');
    div.innerHTML = `<div class="dot"></div><span>${opt.label}</span>`;
    div.onclick = () => select(q.id, opt.value);
    list.appendChild(div);
  }

  // nav
  document.getElementById('btnPrev').disabled = current === 0;
  document.getElementById('btnNext').disabled = !answers[q.id];
  const isLast = current === total - 1;
  document.getElementById('btnNext').textContent = isLast ? 'Finish ✓' : 'Next →';

  // chips for answered questions
  renderChips();
}

function renderChips() {
  const container = document.getElementById('answeredList');
  container.innerHTML = '';
  for (let i = 0; i < current; i++) {
    const q = questions[i];
    const v = answers[q.id];
    if (!v) continue;
    const opt = q.options.find(o => o.value === v);
    const chip = document.createElement('div');
    chip.className = 'chip';
    chip.title = q.text;
    chip.innerHTML = `<span class="chip-label">${q.short}:</span> ${opt ? opt.label.split(' ')[0] : v}`;
    chip.onclick = () => { current = i; renderQ(); };
    container.appendChild(chip);
  }
}

function select(qid, value) {
  answers[qid] = value;
  renderQ();
  fetchResults();
}

function nav(dir) {
  const next = current + dir;
  if (next < 0 || next > questions.length - 1) return;
  current = next;
  renderQ();
  if (Object.keys(answers).length > 0) fetchResults();
}

async function fetchResults() {
  if (loading) return;
  loading = true;
  const panel = document.getElementById('resultsPanel');
  // show spinner while keeping old content
  let spinnerDiv = document.getElementById('liveSpinner');
  if (!spinnerDiv) {
    spinnerDiv = document.createElement('div');
    spinnerDiv.id = 'liveSpinner';
    spinnerDiv.style.cssText = 'position:fixed;top:14px;right:20px;z-index:999';
    spinnerDiv.innerHTML = '<div class="spinner"></div>';
    document.body.appendChild(spinnerDiv);
  }
  spinnerDiv.style.display = 'block';

  try {
    const resp = await fetch('/api/recommend', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({answers}),
    });
    const data = await resp.json();
    renderResults(data);
  } catch(e) {
    console.error(e);
  } finally {
    loading = false;
    if (spinnerDiv) spinnerDiv.style.display = 'none';
  }
}

function renderResults(data) {
  const answered = Object.keys(answers).length;
  const total = questions.length;
  const done = answered >= total;

  let html = '';

  if (done) {
    html += `<div class="done-banner">✓ All questions answered — this is your full recommendation</div>`;
  }

  html += `<div class="result-header">
    <h2>Stage ${data.maturity_stage}</h2>
    <span class="maturity-badge">${data.maturity_label}</span>
  </div>`;

  if (data.stack && data.stack.length) {
    html += `<div class="section-title">🔷 Tool Stack</div>`;
    for (const layer of data.stack) {
      const pri = layer.priority;
      html += `<div class="layer-card ${pri}">
        <div class="layer-top">
          <span class="layer-badge ${pri}">${pri}</span>
          <span class="layer-name">${layer.layer} — ${layer.layer_label}</span>
        </div>
        <div class="layer-why">${layer.why}</div>`;
      for (const t of layer.tools) {
        const pct = Math.round(t.score * 100);
        const gh = t.url.replace('https://github.com/','');
        html += `<div class="tool-row">
          <span class="tool-score">${pct}%</span>
          <span class="tool-name">${t.name}</span>
          <a class="tool-link" href="${t.url}" target="_blank">${gh} ↗</a>
        </div>`;
      }
      html += `</div>`;
    }
  }

  if (data.core_agent_fit && data.core_agent_fit.length) {
    const fits = data.core_agent_fit.filter(f => f.fit_score > 0);
    if (fits.length) {
      html += `<div class="section-title">🔶 Core Agent + LLM</div>`;
      for (const fit of fits) {
        const pct = Math.round(fit.fit_score * 100);
        html += `<div class="agent-card">
          <div class="agent-top">
            <span class="agent-name">${fit.agent} + ${fit.llm}</span>
            <span class="score-pill">${pct}%</span>
          </div>`;
        if (fit.maturity_note) html += `<div class="agent-note">${fit.maturity_note}</div>`;
        html += `<div class="agent-why">${(fit.why||[]).map(w=>`✓ ${w}`).join('<br>')}</div>
        </div>`;
      }
    }
  }

  if (data.next_step_hint) {
    html += `<div class="section-title">📌 Next Step</div>
    <div class="next-step">${data.next_step_hint}</div>`;
  }

  document.getElementById('resultsPanel').innerHTML = html;
}

init();
</script>
</body>
</html>"""


class _Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass  # suppress access logs

    def _send_json(self, data, status=200):
        body = json.dumps(data, ensure_ascii=False).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_html(self, html: str):
        body = html.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/api/questions":
            path = pathlib.Path(__file__).parent / "data" / "org_questions.json"
            data = json.loads(path.read_text())
            self._send_json(data["questions"])
        else:
            self._send_html(_HTML)

    def do_POST(self):
        parsed = urlparse(self.path)
        if parsed.path == "/api/recommend":
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length))
            answers = body.get("answers", {})

            from .org_scorer import build_profile_from_answers, org_recommend
            profile = build_profile_from_answers(answers)
            result = org_recommend(profile, top_per_layer=3)
            self._send_json(asdict(result))
        else:
            self.send_response(404)
            self.end_headers()


def serve(port: int = 7771, open_browser: bool = True):
    server = HTTPServer(("127.0.0.1", port), _Handler)
    url = f"http://localhost:{port}"
    print(f"clawfit UI → {url}")
    if open_browser:
        threading.Timer(0.5, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
