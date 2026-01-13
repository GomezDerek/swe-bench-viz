# AI Benchmarks 2025

Interactive visualization tracking frontier AI model performance on SWE-Bench Verified throughout 2025.

## The AI Coding Race

This project visualizes the competitive landscape of AI coding capabilities across leading AI labs: OpenAI, Anthropic, Google, and xAI. The chart tracks how each vendor's latest models perform on the SWE-Bench Verified benchmark - a real-world test of AI's ability to resolve GitHub issues.

## What's Inside

- **Interactive Chart** - Plotly-powered visualization with model-specific tooltips
- **2025 Timeline Data** - Performance metrics from February through December 2025
- **Auto-Reload Development Server** - File watcher that regenerates the chart on data changes

## Data Highlights

- **Top Performers**: Claude Opus 4.5 (80.9%), GPT-5.2 Thinking (80.0%)
- **12 Major Releases** tracked across 4 vendors
- **Performance Range**: 38% to 80.9% on SWE-Bench Verified

## Files

- `benchmark_chart.html` - The interactive visualization
- `AI_benchmarks_2025.csv` - Raw timeline data
- `plot_ai_benchmarks.py` - Chart generation script
- `watch_and_serve.py` - Development server with auto-reload
- `gpt-benchmarks-sources.txt` - Source URLs for OpenAI claims

## Quick Start

```bash
# Install dependencies
pip install pandas plotly

# Generate chart
python plot_ai_benchmarks.py

# Run dev server with auto-reload
python watch_and_serve.py
# Visit http://localhost:8000/benchmark_chart.html
```

## The Race

The visualization reveals the intense competition in AI coding capabilities throughout 2025, with Anthropic and OpenAI trading leadership positions. Claude Opus 4.5 currently holds the top spot at 80.9%, narrowly ahead of GPT-5.2 Thinking at 80.0%.
