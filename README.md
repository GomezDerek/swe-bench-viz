# AI Benchmarks 2025

Interactive visualizations tracking the race for AI coding supremacy between OpenAI, Anthropic, Google, xAI, and DeepSeek.

## 📊 Live Visualizations

### [SWE-Bench Verified (2025)](https://gomezderek.github.io/swe-bench-viz/chart.html)
Real-world GitHub issue resolution throughout 2025. Watch Anthropic and OpenAI trade leadership positions, culminating in Claude Opus 4.5 (80.9%) narrowly edging out GPT-5.2 Thinking (80.0%).

**Key Insight**: Performance more than doubled in 9 months—from 38% (GPT-4.5 in February) to 80.9% (Claude Opus 4.5 in November).

**[→ View Interactive Chart](https://gomezderek.github.io/swe-bench-viz/chart.html)**

### [HumanEval Evolution (2021-2025)](https://gomezderek.github.io/swe-bench-viz/humaneval_chart.html)
Four years of code generation progress from Codex (28.8% in 2021) to o1 (92.4% in 2025).

**Key Insight**: AI coding ability improved **3.2x** in 4 years.

**[→ View Interactive Chart](https://gomezderek.github.io/swe-bench-viz/humaneval_chart.html)**

## 🏆 The Race (2021-2025)

### The Early Years: Code Generation (2021-2023)
The AI coding race began with **HumanEval**, where models learned to write Python functions from scratch:

- **2021**: OpenAI's Codex (28.8%) established that LLMs could generate code, powering the first GitHub Copilot
- **2022**: GPT-3.5 (48.1%) nearly doubled performance, crossing the 50% threshold
- **2023**: GPT-4 (67%) and Claude 2 (70%) demonstrated that AI could solve 2 out of 3 problems correctly

**Key Milestone**: By 2023, AI coding assistants became genuinely useful for basic function writing.

### The Acceleration: Approaching Human-Level (2024)
- **Claude 3.5 Sonnet** (92%) broke the 90% barrier, showing AI could solve 9 out of 10 isolated coding problems
- HumanEval scores plateaued near human-level performance, signaling the need for harder benchmarks

### The Modern Era: Real-World Software Engineering (2025)
With code generation largely solved, the race shifted to **SWE-Bench Verified**—resolving real GitHub issues in production codebases. This year saw unprecedented competition:

**Breakthrough Releases (SWE-Bench Verified):**
1. **GPT-4.5** (Feb) — 38.0% - Established baseline for real-world SWE tasks
2. **o3/o4-mini** (Apr) — 71.7% - Nearly doubled performance in 2 months, first to break 70%
3. **GPT-5** (Aug) — 74.9% - Extended OpenAI's lead
4. **Claude Sonnet 4.5** (Oct) — 77.2% - Anthropic takes the crown
5. **Claude Opus 4.5** (Nov) — 80.9% - First to break 80%
6. **GPT-5.2 Thinking** (Dec) — 80.0% - OpenAI nearly matches the leader

**The 2025 Story**: OpenAI and Anthropic traded leadership positions throughout the year, with performance more than doubling from February to November. The rapid improvement (38% → 80.9%) suggests AI is approaching practical utility for real-world software engineering tasks.

### What Changed?
- **2021-2024**: Focus on code generation and isolated problem-solving
- **2025**: Shift to real-world software engineering—understanding large codebases, debugging production code, and generating complete pull requests
- **Result**: AI coding capability improved 3.2x on HumanEval (2021-2025) and 2.1x on SWE-Bench Verified (just in 2025)

## 📖 Understanding the Benchmarks

### What is SWE-Bench Verified?
**SWE-Bench Verified** tests AI models on real-world software engineering tasks by having them resolve actual GitHub issues from popular open-source projects. Each test presents the AI with a bug report or feature request, the codebase, and asks it to generate a pull request that fixes the issue. The benchmark measures what percentage of issues the AI successfully resolves.

**Timeline**: Introduced in 2024, SWE-Bench Verified became the gold standard for measuring AI's ability to handle real software engineering work. Our visualization tracks the 2025 timeline (February-December) as frontier models from OpenAI, Anthropic, Google, and xAI competed for the top spot.

**Why It Matters**: Unlike synthetic coding tests, SWE-Bench Verified uses real issues from real codebases—it measures whether AI can actually help with day-to-day software engineering work, not just solve isolated programming puzzles.

[→ Read more about SWE-Bench Verified](https://openai.com/index/introducing-swe-bench-verified/)

### What is HumanEval?
**HumanEval** is a classic code generation benchmark where AI models write Python functions to pass a set of unit tests. Each of the 164 problems includes a function signature, docstring description, and test cases. The "pass@1" metric measures how often the model's first attempt produces code that passes all tests.

**Timeline**: Created by OpenAI in 2021 alongside Codex (the original GitHub Copilot model), HumanEval has tracked AI coding progress for 4+ years. Our visualization spans 2021-2025, showing the evolution from early models that barely solved 1 in 4 problems to modern models that solve 9 in 10.

**Why It Matters**: HumanEval provides a consistent measuring stick across years and vendors. While it's simpler than real-world coding (each problem is self-contained), it clearly shows how AI code generation has improved—and when major breakthroughs happened.

[→ Read more about HumanEval](https://www.deepchecks.com/glossary/humaneval/)

---
I also suggest this fantastic article (10 min read) on the evolution of coding benchmarks from 2021-2025: [Understanding LLM Code Benchmarks: From HumanEval to SWE-bench](https://runloop.ai/blog/understanding-llm-code-benchmarks-from-humaneval-to-swe-bench)


## 📁 What's Inside This Repo

- **Curated Benchmark Datasets** — 286 verified results across 51 datasets (coding, vision, OCR, reasoning)
- **Interactive Plotly Charts** — Vendor-color-coded visualizations with model-specific tooltips
- **Python Visualization Scripts** — Automated chart generation from CSV/JSON data
- **Source Documentation** — All data sourced from official vendor announcements, research papers, and verified leaderboards

## 🔗 Data Sources

All benchmark scores verified from official sources:

### Official Vendor Announcements
- **OpenAI**: [Research Index](https://openai.com/research/) - Model release announcements and technical papers
- **Anthropic**: [News & Updates](https://www.anthropic.com/news) - Claude system cards and release announcements
- **Google DeepMind**: [Research Blog](https://blog.google/technology/ai/google-deepmind/) - Gemini technical reports and model cards
- **DeepSeek**: [API Documentation Updates](https://api-docs.deepseek.com/news/news250114) - Official benchmark results and changelogs


### Verified Leaderboards
- **AlphaXiv**: Community-maintained leaderboard aggregating verified benchmark results
- Cross-references vendor claims with independent verification where available

### Technical Reports
- Model system cards (safety evaluations, capability assessments)
- Vendor technical documentation (API reference guides, model specifications)
- Independent evaluation reports from research institutions


## 💻 Run Locally

For devs who want to play with the charts and explore the data:

```bash
# Clone repository
git clone https://github.com/GomezDerek/swe-bench-viz.git
cd swe-bench-viz

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Generate charts
python plot_ai_benchmarks.py          # → chart.html
python plot_humaneval_benchmarks.py   # → humaneval_chart.html

# Optional: Run dev server with auto-reload
python utils/watch_and_serve.py
# Visit http://localhost:8000/[chart_name].html
```

See [CLAUDE.md](CLAUDE.md) for complete documentation on data structure, typical workflows, and utility scripts.
