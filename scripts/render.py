"""Render the profile README's SVG cards into assets/.

hero.svg and trace.svg are static designs. heatmap.svg and stats.svg come from
live GitHub data and are refreshed by the daily workflow. Stdlib only.
"""
import datetime as dt
import json
import os
import urllib.parse
import urllib.request
from html import escape
from pathlib import Path

LOGIN = "ayanpandey"
OUT = Path(__file__).resolve().parent.parent / "assets"

# Portfolio palette (ayanpandey.xyz) on a dark plum terminal.
BG, EDGE, PANEL = "#1b1726", "#3d3349", "#221c2f"
INK, MUTED, DIM = "#f1e7da", "#a89bb4", "#6b6178"
VIOLET, PINK, GOLD, MINT = "#c0a3e6", "#f08f84", "#e0b45a", "#7fcbb0"
RAMP = ["#2a2236", "#4b3470", "#6e4a9e", "#9b74cc", "#c0a3e6"]
FONT = "'JetBrains Mono','SFMono-Regular',ui-monospace,Menlo,Consolas,monospace"


def frame(w, h, title, body, extra_style=""):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(title)}">
<style>
  text {{ font-family: {FONT}; }}
  .ink {{ fill: {INK}; }} .muted {{ fill: {MUTED}; }} .dim {{ fill: {DIM}; }}
  .violet {{ fill: {VIOLET}; }} .pink {{ fill: {PINK}; }} .gold {{ fill: {GOLD}; }} .mint {{ fill: {MINT}; }}
  {extra_style}
</style>
<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="14" fill="{BG}" stroke="{EDGE}"/>
<circle cx="24" cy="22" r="6" fill="{PINK}"/><circle cx="44" cy="22" r="6" fill="{GOLD}"/><circle cx="64" cy="22" r="6" fill="{MINT}"/>
<text x="{w/2}" y="27" text-anchor="middle" font-size="12" class="dim">{escape(title)}</text>
<line x1="0" y1="44" x2="{w}" y2="44" stroke="{EDGE}"/>
{body}
</svg>
"""


def typed(x, y, parts, start, dur, size=15, clip_id="c"):
    """A line that types itself in: a clip rect grows in steps from 0 to full width."""
    chars = sum(len(t) for t, _ in parts)
    width = chars * size * 0.61 + 4
    spans = "".join(f'<tspan class="{cls}">{escape(t)}</tspan>' for t, cls in parts)
    return f"""<clipPath id="{clip_id}"><rect x="{x}" y="{y-size}" width="0" height="{size*1.6}">
  <animate attributeName="width" from="0" to="{width:.0f}" begin="{start}s" dur="{dur}s" calcMode="discrete" values="{';'.join(str(round(width*i/max(chars,1))) for i in range(chars+1))}" fill="freeze"/>
</rect></clipPath>
<text x="{x}" y="{y}" font-size="{size}" xml:space="preserve" clip-path="url(#{clip_id})">{spans}</text>"""


def shown(x, y, parts, start, size=15):
    """An output line that appears at once, like a command's result."""
    spans = "".join(f'<tspan class="{cls}">{escape(t)}</tspan>' for t, cls in parts)
    return f"""<text x="{x}" y="{y}" font-size="{size}" xml:space="preserve" opacity="0">{spans}
  <animate attributeName="opacity" from="0" to="1" begin="{start}s" dur="0.15s" fill="freeze"/></text>"""


def void_cat(x, y, s):
    """Void, the portfolio's black cat: blinks, glances at the terminal, flicks its tail."""
    return f"""<g transform="translate({x} {y}) scale({s})">
  <path d="M46 52 C64 50 70 34 62 24" fill="none" stroke="#120e18" stroke-width="5" stroke-linecap="round">
    <animateTransform attributeName="transform" type="rotate" values="0 46 52;9 46 52;0 46 52;-4 46 52;0 46 52" dur="3.2s" repeatCount="indefinite"/>
  </path>
  <ellipse cx="32" cy="57" rx="19" ry="7" fill="#120e18"/>
  <path d="M12 30 L10 6 L28 20 Z M52 30 L54 6 L36 20 Z" fill="#120e18"/>
  <path d="M14 26 L13 12 L23 20 Z M50 26 L51 12 L41 20 Z" fill="{PINK}" opacity="0.55"/>
  <ellipse cx="32" cy="36" rx="22" ry="19" fill="#120e18"/>
  <g>
    <ellipse cx="23" cy="33" rx="7" ry="7" fill="#fff"><animate attributeName="ry" values="7;7;0.6;7;7" keyTimes="0;0.9;0.94;0.98;1" dur="4.5s" repeatCount="indefinite"/></ellipse>
    <ellipse cx="41" cy="33" rx="7" ry="7" fill="#fff"><animate attributeName="ry" values="7;7;0.6;7;7" keyTimes="0;0.9;0.94;0.98;1" dur="4.5s" repeatCount="indefinite"/></ellipse>
    <g>
      <circle cx="23" cy="34" r="4.2" fill="#2a1733"/><circle cx="41" cy="34" r="4.2" fill="#2a1733"/>
      <circle cx="21.6" cy="32.4" r="1.3" fill="#fff"/><circle cx="39.6" cy="32.4" r="1.3" fill="#fff"/>
      <animateTransform attributeName="transform" type="translate" values="0 0;-2.4 0.6;-2.4 0.6;0.8 0;0 0" keyTimes="0;0.2;0.6;0.8;1" dur="7s" repeatCount="indefinite"/>
    </g>
  </g>
  <path d="M29.5 43 L34.5 43 L32 46 Z" fill="{PINK}"/>
  <path d="M8 40 L18 41 M8 45 L18 44 M56 40 L46 41 M56 45 L46 44" stroke="#3d3349" stroke-width="1.2" stroke-linecap="round"/>
</g>"""


def hero():
    w, h, x = 880, 344, 32
    t = 0.4
    rows = []
    script = [
        ("cmd", [("❯ ", "pink"), ("whoami", "ink")]),
        ("out", [("Ayan", "violet"), (" · AI Engineer @ ", "ink"), ("Northstarz", "gold"), (" · Bangalore, India", "muted")]),
        ("cmd", [("❯ ", "pink"), ("cat focus.txt", "ink")]),
        ("out", [("▸ ", "mint"), ("multi-agent assistants    ", "ink"), ("▸ ", "mint"), ("hybrid search + RAG", "ink")]),
        ("out", [("▸ ", "mint"), ("real-time voice AI        ", "ink"), ("▸ ", "mint"), ("LLM evaluation", "ink")]),
        ("cmd", [("❯ ", "pink"), ("./status --now", "ink")]),
        ("out", [("● ", "mint"), ("shipping recruiting agents in Go + Python", "ink")]),
        ("out", [("● ", "gold"), ("open to AI engineering roles + consulting", "ink")]),
    ]
    y = 82
    for i, (kind, parts) in enumerate(script):
        if kind == "cmd":
            n = sum(len(p) for p, _ in parts)
            rows.append(typed(x, y, parts, t, n * 0.055, clip_id=f"l{i}"))
            t += n * 0.055 + 0.35
        else:
            rows.append(shown(x, y, parts, t))
            t += 0.12
        y += 29
        if kind == "out" and (i + 1 == len(script) or script[i + 1][0] == "cmd"):
            t += 0.5
    rows.append(f"""<text x="{x}" y="{y}" font-size="15" opacity="0"><tspan class="pink">❯ </tspan><tspan class="violet">▍</tspan>
  <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.01;0.5;0.51" begin="{t}s" dur="1s" repeatCount="indefinite"/></text>""")
    body = "\n".join(rows) + void_cat(705, 160, 2.2) + f"""
<text x="775" y="324" text-anchor="middle" font-size="11" class="dim">void · head of QA</text>"""
    return frame(w, h, "ayan@northstarz: ~ — zsh", body)


def trace():
    w, h = 880, 400
    stages = [
        ("sourcing", "3,800 profiles/run", "LinkedIn + pool"),
        ("screening", "0 errs · 70 gates", "2-stage LLM scoring"),
        ("ranking", "BM25+dense · RRF", "ColBERT v2 re-rank"),
        ("interview", "~150 / month", "voice · EN·HI·KN"),
        ("outreach", "Gemini Live", "Twilio · WhatsApp"),
    ]
    box_w, gap, top = 152, 14, 196
    left = (w - (len(stages) * box_w + (len(stages) - 1) * gap)) / 2
    parts = [f"""<text x="32" y="76" font-size="15"><tspan class="pink">❯ </tspan><tspan class="ink">trace recruiter-agent --live</tspan></text>
<text x="848" y="76" font-size="12" text-anchor="end" class="mint">● live
  <animate attributeName="opacity" values="1;0.35;1" dur="1.6s" repeatCount="indefinite"/></text>
<rect x="290" y="98" width="300" height="52" rx="10" fill="{PANEL}" stroke="{VIOLET}"/>
<text x="440" y="121" text-anchor="middle" font-size="15" class="violet" font-weight="700">orchestrator</text>
<text x="440" y="140" text-anchor="middle" font-size="11" class="muted">Go · Google ADK · multi-agent</text>"""]
    centers = []
    for i, (name, metric, sub) in enumerate(stages):
        bx = left + i * (box_w + gap)
        cx = bx + box_w / 2
        centers.append(cx)
        parts.append(f"""<path d="M440 150 C440 172 {cx} 170 {cx} {top}" fill="none" stroke="{EDGE}" stroke-dasharray="3 4"/>
<rect x="{bx}" y="{top}" width="{box_w}" height="78" rx="10" fill="{PANEL}" stroke="{EDGE}">
  <animate attributeName="stroke" values="{EDGE};{PINK};{EDGE};{EDGE}" keyTimes="0;0.06;0.22;1" begin="{i*0.75:.2f}s" dur="3s" repeatCount="indefinite"/>
</rect>
<text x="{cx}" y="{top+24}" text-anchor="middle" font-size="14" class="ink" font-weight="700">{name}</text>
<text x="{cx}" y="{top+46}" text-anchor="middle" font-size="11" class="gold">{escape(metric)}</text>
<text x="{cx}" y="{top+64}" text-anchor="middle" font-size="10.5" class="muted">{escape(sub)}</text>""")
    lane = top + 98
    parts.append(f'<line x1="{centers[0]}" y1="{lane}" x2="{centers[-1]}" y2="{lane}" stroke="{EDGE}"/>')
    for c in centers:
        parts.append(f'<line x1="{c}" y1="{top+78}" x2="{c}" y2="{lane}" stroke="{EDGE}"/>')
    for k in range(4):
        parts.append(f"""<circle r="4" fill="{PINK if k % 2 else VIOLET}">
  <animateMotion dur="3s" begin="{k*0.75}s" repeatCount="indefinite" path="M{centers[0]} {lane} L{centers[-1]} {lane}"/></circle>""")
    stats = [("30+", "companies served"), ("600+", "positions closed"), ("300%", "revenue growth · 3 mo"), ("−98%", "cost / match · $0.24→$0.005")]
    sx = 32
    for i, (num, label) in enumerate(stats):
        x = sx + i * 212
        parts.append(f"""<text x="{x}" y="{lane+48}" font-size="22" class="violet" font-weight="700">{escape(num)}</text>
<text x="{x}" y="{lane+66}" font-size="11" class="muted">{escape(label)}</text>""")
    parts.append(f"""<text x="848" y="{h-14}" text-anchor="end" font-size="10.5" class="dim">eval harness: 200-query live suite · 100% pass · gates every change</text>""")
    return frame(w, h, "northstarz / recruiter-agent — trace", "\n".join(parts))


# ---------- live data ----------


def gh_graphql(query, variables):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query, "variables": variables}).encode(),
        headers={"Authorization": "Bearer " + os.environ["GITHUB_TOKEN"], "User-Agent": "profile-render"})
    with urllib.request.urlopen(req, timeout=30) as r:
        out = json.load(r)
    if out.get("errors"):
        raise SystemExit(out["errors"])
    return out["data"]


def gh_search_count(q):
    url = "https://api.github.com/search/issues?per_page=1&q=" + urllib.parse.quote(q)
    req = urllib.request.Request(url, headers={"Authorization": "Bearer " + os.environ["GITHUB_TOKEN"], "User-Agent": "profile-render"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)["total_count"]


def fetch():
    data = gh_graphql("""query($login: String!) { user(login: $login) {
      contributionsCollection { contributionCalendar { totalContributions
        weeks { contributionDays { date contributionCount } } } } } }""", {"login": LOGIN})
    weeks = data["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    days = [(dt.date.fromisoformat(d["date"]), d["contributionCount"]) for w in weeks for d in w["contributionDays"]]
    return {
        "weeks": weeks,
        "days": days,
        "total": data["user"]["contributionsCollection"]["contributionCalendar"]["totalContributions"],
        "merged": gh_search_count(f"is:pr is:merged author:{LOGIN} -user:{LOGIN}"),
        "opened": gh_search_count(f"is:pr author:{LOGIN} -user:{LOGIN}"),
    }


def streaks(days):
    today = dt.date.today()
    counts = {d: c for d, c in days}
    cur, d = 0, today if counts.get(today) else today - dt.timedelta(days=1)
    while counts.get(d):
        cur += 1
        d -= dt.timedelta(days=1)
    best = run = 0
    for _, c in days:
        run = run + 1 if c else 0
        best = max(best, run)
    active = sum(1 for _, c in days if c)
    return cur, best, active


def heatmap(data):
    cell, gap, x0, y0 = 12, 3, 58, 108
    weeks = data["weeks"]
    peak = max((c for _, c in data["days"]), default=0) or 1
    rects, months, last_month = [], [], None
    for wi, w in enumerate(weeks):
        for d in w["contributionDays"]:
            date = dt.date.fromisoformat(d["date"])
            c = d["contributionCount"]
            lvl = 0 if c == 0 else min(4, 1 + int(3 * c / peak + 0.5))
            x, y = x0 + wi * (cell + gap), y0 + date.isoweekday() % 7 * (cell + gap)
            rects.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="2.5" fill="{RAMP[lvl]}" style="animation-delay:{(wi + date.isoweekday() % 7) * 0.018:.3f}s"><title>{date}: {c}</title></rect>')
            if date.day <= 7 and date.month != last_month and date.isoweekday() % 7 == 0:
                months.append(f'<text x="{x}" y="{y0-10}" font-size="10" class="dim">{date.strftime("%b").lower()}</text>')
                last_month = date.month
    labels = "".join(f'<text x="{x0-10}" y="{y0 + i*(cell+gap) + 10}" font-size="10" text-anchor="end" class="dim">{n}</text>' for i, n in ((1, "mon"), (3, "wed"), (5, "fri")))
    legend_x = 880 - 32 - 5 * 15 - 70
    legend = f'<text x="{legend_x}" y="232" font-size="10" class="dim">less</text>' + "".join(
        f'<rect x="{legend_x + 30 + i*15}" y="223" width="11" height="11" rx="2.5" fill="{c}"/>' for i, c in enumerate(RAMP)
    ) + f'<text x="{legend_x + 30 + 5*15 + 4}" y="232" font-size="10" class="dim">more</text>'
    head = f"""<text x="32" y="70" font-size="15"><tspan class="pink">❯ </tspan><tspan class="ink">git log --since="1 year" | heatmap</tspan></text>
<text x="848" y="70" text-anchor="end" font-size="12" class="muted"><tspan class="violet" font-weight="700">{data['total']:,}</tspan> contributions</text>"""
    style = "rect[style] { opacity: 0; animation: pop .35s ease-out forwards; } @keyframes pop { from { opacity: 0; transform: translateY(3px); } to { opacity: 1; transform: none; } } @media (prefers-reduced-motion: reduce) { rect[style] { animation: none; opacity: 1; } }"
    return frame(880, 250, f"{LOGIN} — contributions", head + labels + "".join(months) + "".join(rects) + legend, style)


def stats(data):
    cur, best, active = streaks(data["days"])
    rate = f"{data['merged'] * 100 // data['opened']}%" if data["opened"] else "—"
    cards = [
        (f"{cur}", "day streak", "mint"), (f"{best}", "longest streak", "violet"), (f"{active}", "active days / yr", "gold"),
        (f"{data['merged']}", "OSS PRs merged", "pink"), (rate, "merge rate", "violet"),
    ]
    out = [f'<text x="32" y="76" font-size="15"><tspan class="pink">❯ </tspan><tspan class="ink">./stats --refresh daily</tspan></text>']
    cw = (880 - 64 - 4 * 14) / 5
    for i, (num, label, cls) in enumerate(cards):
        x = 32 + i * (cw + 14)
        out.append(f"""<rect x="{x}" y="96" width="{cw:.0f}" height="78" rx="10" fill="{PANEL}" stroke="{EDGE}"/>
<text x="{x + cw/2:.0f}" y="134" text-anchor="middle" font-size="26" font-weight="700" class="{cls}">{escape(num)}</text>
<text x="{x + cw/2:.0f}" y="158" text-anchor="middle" font-size="11" class="muted">{escape(label)}</text>""")
    out.append(f'<text x="848" y="198" text-anchor="end" font-size="10" class="dim">updated {dt.date.today().isoformat()} · github actions</text>')
    return frame(880, 212, f"{LOGIN} — stats", "\n".join(out))


def main():
    OUT.mkdir(exist_ok=True)
    (OUT / "hero.svg").write_text(hero())
    (OUT / "trace.svg").write_text(trace())
    data = fetch()
    (OUT / "heatmap.svg").write_text(heatmap(data))
    (OUT / "stats.svg").write_text(stats(data))
    print("rendered", sorted(p.name for p in OUT.glob("*.svg")))


if __name__ == "__main__":
    main()
