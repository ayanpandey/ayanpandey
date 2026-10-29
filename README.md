<div align="center">

<img src="assets/hero.svg" width="100%" alt="Terminal: whoami → Ayan, AI Engineer at Northstarz, Bangalore. Focus: multi-agent assistants, hybrid search and RAG, real-time voice AI, LLM evaluation. Open to AI engineering roles and consulting. Void the black cat watches from the corner." />

<a href="https://ayanpandey.xyz"><img src="https://img.shields.io/badge/portfolio-ayanpandey.xyz-7b4fa6?style=for-the-badge&labelColor=1b1726" alt="Portfolio" /></a>
<a href="https://linkedin.com/in/ayanpdy"><img src="https://img.shields.io/badge/linkedin-ayanpdy-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=1b1726" alt="LinkedIn" /></a>
<a href="mailto:ayanpdy@gmail.com"><img src="https://img.shields.io/badge/email-ayanpdy@gmail.com-e8746a?style=for-the-badge&logo=gmail&logoColor=white&labelColor=1b1726" alt="Email" /></a>
<img src="https://img.shields.io/badge/status-open_to_AI_roles-7fcbb0?style=for-the-badge&labelColor=1b1726" alt="Open to AI roles" />

<br /><br />

<h3><code>❯ trace recruiter-agent --live</code></h3>

<img src="assets/trace.svg" width="100%" alt="Animated trace of the Northstarz recruiting agent: an orchestrator in Go and Google ADK drives sourcing (3,800 profiles per run), screening (0 errors on a 70-decision gate), ranking (BM25 plus dense with RRF, ColBERT v2 re-rank), interviews (~150 a month in English, Hindi and Kannada) and outreach (Gemini Live over Twilio). 30+ companies, 600+ positions closed, 300% revenue growth in 3 months, 98% lower cost per match." />

</div>

<details>
<summary><b>the long version</b>: what I build at Northstarz</summary>
<br />

- **Multi-agent recruiting assistant**: Go + Google ADK (migrated from LangChain). It handles sourcing, screening, outreach, evaluation and scheduling, and has helped 30+ companies close 600+ positions.
- **Candidate search**: Gemini embeddings in Qdrant, hybrid dense + BM25 with Reciprocal Rank Fusion, ColBERT v2 re-ranking and LLM scoring. A 200-query live eval suite gates every change.
- **Voice AI**: a Gemini Live calling agent over Twilio, a WebSocket AI interviewer in English, Hindi and Kannada, and a WebRTC interview room with Go signalling and a self-hosted TURN server.
- **AnthroSense**: 13 BiLSTM trait models trained in PyTorch and served from Go via ONNX, at zero per-call LLM cost.
- **Cost**: incremental scoring, Flex-tier inference and model routing cut talent-matching cost from $0.24 to $0.005 per match.

</details>

<div align="center">

<h3><code>❯ ls ~/side-projects</code></h3>

</div>

| | project | what it does |
|---|---|---|
| 🧭 | [**job-application-agent**](https://github.com/ayanpandey/job-application-agent) | Finds matching jobs, tailors the resume per role (an auditor pass blocks factual drift), fills applications, drafts recruiter notes |
| 🕸️ | **Agent Hub** | Runs Claude, Codex and Gemini as one coding-agent pool: shared SQLite blackboard, deterministic routing, a "needs you" queue |
| 🎬 | **Hermes AI Reels Studio** | Topic in, published vertical reel out: Gemini script, Veo 3.1 clips, TTS, word-synced captions |
| 🐈‍⬛ | [**Void**](https://ayanpandey.xyz) | The cat-shaped guide on my portfolio: ask it anything about my work |
| 🔤 | [**nanoGPT**](https://github.com/ayan20186/nanoGPT) | GPT-2 from scratch in PyTorch, trained on Shakespeare |
| 🍲 | [**Novel Recipe Generation**](https://github.com/ayan20186/Novel-Recipe-Generation-Constraint-Optimization) | GPT-2 / Mistral / LLaMA-3 on 118k recipes, validated by actually cooking them |

<div align="center">

<h3><code>❯ git log --since="1 year" | heatmap</code></h3>

<img src="assets/heatmap.svg" width="100%" alt="Contribution heatmap for the last year, refreshed daily." />
<img src="assets/stats.svg" width="100%" alt="Streaks, active days and merged open-source PRs, refreshed daily." />

<h3><code>❯ git log --merged --author=ayanpandey --not ~/own-repos</code></h3>

</div>

<!-- OSS:START -->
_First merged contributions coming soon._
<!-- OSS:END -->

<div align="center">

<h3><code>❯ cat stack.txt</code></h3>

<img src="https://skillicons.dev/icons?i=go,py,ts,react,pytorch,fastapi,gcp,aws,docker,redis,mongodb,nginx,linux,cpp,java&theme=dark&perline=15" alt="Go, Python, TypeScript, React, PyTorch, FastAPI, GCP, AWS, Docker, Redis, MongoDB, Nginx, Linux, C++, Java" />

<sub>also: Google ADK · LangChain · ONNX · Vertex AI · Gemini · Qdrant · ColBERT · NATS JetStream · WebRTC · Twilio</sub>

<h3><code>❯ history | tail -3</code></h3>

<sub><b>ML Engineer @ Wishfin</b>: loan-eligibility scoring that lifted partner-bank conversions 70%</sub><br />
<sub><b>Research Assistant @ MIDAS Lab, IIIT-Delhi</b>: YOLOv8 product-image extraction, 87% accuracy</sub><br />
<sub><b>B.Tech ECE @ IIIT Delhi</b></sub>

<br /><br />

<sub>void reviewed this README · 0 bugs found · cards redrawn daily by github actions</sub>

</div>
