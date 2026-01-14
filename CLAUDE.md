# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains benchmark data for AI/ML models in multiple formats.

### Directory Structure
```
swe_benchmarks/
├── data/                           # All benchmark data files
│   ├── AI_benchmarks_2025.csv
│   ├── benchmarks.json
│   ├── humaneval_benchmarks.json
│   ├── gpt-benchmarks-2025.json
│   └── gpt-benchmarks-sources.txt
├── utils/                          # Utility scripts (portable)
│   ├── compare_data.py
│   └── watch_and_serve.py
├── plot_ai_benchmarks.py          # Main chart generation scripts
├── plot_humaneval_benchmarks.py
├── chart.html                      # Generated visualization files
├── humaneval_chart.html
├── benchmark_chart.html
├── requirements.txt
├── CLAUDE.md
└── README.md
```

### Data Files (in `data/` directory)
- **`data/benchmarks.json`** - Comprehensive database of 286 verified results + 36 pending verifications across multiple benchmark categories (last updated: 2025-12-21)
- **`data/AI_benchmarks_2025.csv`** - Timeline data tracking frontier model performance across 2025 (Feb-Dec)
- **`data/humaneval_benchmarks.json`** - Curated historical dataset of HumanEval pass@1 scores from 2021-2025 (15 data points)
- **`data/gpt-benchmarks-2025.json`** - Focused collection of OpenAI model benchmarks (GPT-4.5 through GPT-5.2)
- **`data/gpt-benchmarks-sources.txt`** - Source URLs for OpenAI benchmark claims

### Scripts
- **`plot_ai_benchmarks.py`** - Generates SWE-Bench Verified chart from `data/AI_benchmarks_2025.csv`
- **`plot_humaneval_benchmarks.py`** - Generates HumanEval historical chart from `data/humaneval_benchmarks.json`
- **`requirements.txt`** - Python dependencies (pandas, plotly)

### Utility Scripts (in `utils/` directory)
- **`utils/compare_data.py`** - Compares SWE-Bench Verified data between CSV and JSON files (portable, can run from any directory)
- **`utils/watch_and_serve.py`** - Development server with auto-reload for live chart updates (portable, can run from any directory)

**Note**: Both utility scripts use `Path(__file__)` to determine their location and build absolute paths to data files. This means they can be run from anywhere in the repository without changing directories:
```bash
# Run from project root
python utils/compare_data.py
python utils/watch_and_serve.py

# Or with uv
uv run utils/compare_data.py
```

### Chart Files
- **`chart.html`** - Main SWE-Bench Verified visualization (The AI Coding Race 2025)
- **`humaneval_chart.html`** - HumanEval historical trends (2021-2025)
- **`benchmark_chart.html`** - Redirect page to chart.html for convenience

### Data Sources
The repository tracks benchmark performance from:
- OpenAI (GPT-4.5, o3/o4-mini, GPT-5.x series)
- Anthropic (Claude 3.7/4.5 series)
- Google (Gemini 2.5/3 Pro)
- xAI (Grok Code Fast)

## Benchmark Categories

### 1. Coding & Software Engineering
- **HumanEval** (5 entries) - Python code generation benchmark using pass@1 metric
  - Top scores: o1-preview (92.4%), claude-35-sonnet (92.0%), gpt-4o (90.2%)
  - All entries from: 2025-12-17
- **MBPP** (2 entries) - Mostly Basic Python Problems using pass@1 metric
  - Top scores: claude-35-sonnet (89.2%), gpt-4o (87.8%)
  - All entries from: 2025-12-17
- **SWE-Bench-Verified** (3 verified + 8 pending) - Real-world GitHub issue resolution
  - Top scores: claude-sonnet-4-high-compute (82.0%), claude-sonnet-4 (77.2%)
  - Date range: 2025-12-17 to 2025-12-24
  - Note: Metric differences exist (resolve-rate vs accuracy)

### 2. Computer Vision
- ImageNet-1K/V2, CIFAR-10/100, COCO, ADE20K
- MVTec-AD (anomaly detection), VISA
- NEU-DET, Severstal Steel (industrial defect detection)

### 3. OCR & Document Parsing
- OmniDocBench, OCRBench-v2, ThaiOCRBench, OlmOCR-Bench
- CC-OCR, MME-VideoOCR, Kitab-Bench
- CodeSOTA verification benchmarks

### 4. Language Understanding & Reasoning
- **Math**: GSM8K, MATH, AIME-2024, SVAMP, MAWPS
- **General Knowledge**: MMLU, GPQA
- **Common Sense**: HellaSwag, Winogrande, CommonsenseQA, StrategyQA
- **Logic**: LogiQA, ReClor
- **Reading Comprehension**: HotpotQA, ARC-Challenge

### 5. Medical Imaging
- **Chest X-ray**: ChexPert, MIMIC-CXR, NIH-ChestXray14, VinDr-CXR, RSNA-Pneumonia, COVID-ChestXray
- **MRI**: ABIDE-I, ABIDE-II
- PadChest

### 6. Reinforcement Learning
- Atari-2600

## Timeline Data (CSV Format)

### AI_benchmarks_2025.csv Structure
The CSV file tracks frontier model performance over time with the following columns:
- **`date`** - Release/update date (MM-DD-YYYY format)
- **`model`** - Model name (e.g., "Claude Sonnet 4.5", "GPT-5.2 Thinking")
- **`vendor`** - Company/organization (OpenAI, Anthropic, Google, xAI)
- **`swe_bench_verified`** - SWE-Bench Verified score (%)
- **`osworld`** - OSWorld benchmark score (%)
- **`terminal_bench_2.0`** - Terminal Bench 2.0 score (%)
- **`vending_bench_t2`** - Vending Bench T2 score (%)

### Notable Performance Metrics (2025)
- **Top SWE-Bench Verified**: Claude Opus 4.5 (80.9%), GPT-5.2 Thinking (80.0%), Claude Sonnet 4.5 (77.2%)
- **Agentic Benchmarks**: Claude Opus 4.5 leads in OSWorld (66.3%), Terminal Bench (59.3%), and Vending Bench (54.8%)

### Visualization Script
The `plot_ai_benchmarks.py` script creates interactive trend charts:

**Setup:**
```bash
# Install dependencies
pip install -r requirements.txt

# Or install manually
pip install pandas>=2.0.0 plotly>=6.0.0
```

**Usage:**
```bash
python plot_ai_benchmarks.py
```

**Output:**
- Interactive Plotly chart showing SWE-Bench Verified trends by vendor
- Overlay of agentic benchmark performance over time
- Color-coded by vendor: OpenAI (teal), Anthropic (coral), Google (blue), xAI (black), DeepSeek (blue)
- Opens automatically in default browser
- Saves to `chart.html`

### HumanEval Visualization Script
The `plot_humaneval_benchmarks.py` script creates a historical trend chart for HumanEval pass@1 scores:

**Data Source:**
- Uses `humaneval_benchmarks.json` (15 historical data points from 2021-2025)

**Usage:**
```bash
python plot_humaneval_benchmarks.py
```

**Output:**
- Interactive Plotly chart showing HumanEval evolution from 2021-2025
- Tracks progression from Codex (28.8%) to modern models (92.4%)
- Same vendor color scheme as main chart
- Includes annotation marking HumanEval's release (July 2021)
- Saves to `humaneval_chart.html`

**Key Milestones Tracked:**
- 2021: Codex (28.8%), GPT-3 (0%)
- 2022: GPT-3.5 (48.1%)
- 2023: GPT-4 (67%), Claude 2 (70%)
- 2024: Claude 3.5 Sonnet (92%), GPT-4o (87.2%)
- 2025: o1 (92.4%), GPT-4o (90.2%)

### Utility Scripts

#### compare_data.py
Analyzes overlaps and discrepancies between `data/AI_benchmarks_2025.csv` and `data/benchmarks.json` for SWE-Bench Verified scores.

**Usage:**
```bash
python utils/compare_data.py
```

**Output:**
- Lists all CSV entries
- Lists verified JSON results
- Lists pending JSON verifications
- Identifies potential matches between datasets
- Provides summary statistics

**Use case**: Quality assurance and data validation when updating benchmark scores.

#### watch_and_serve.py
Development server that watches for file changes and automatically regenerates charts.

**Usage:**
```bash
python utils/watch_and_serve.py
```

**Features:**
- Watches `data/AI_benchmarks_2025.csv` and `plot_ai_benchmarks.py` for changes
- Auto-regenerates `chart.html` when changes detected
- Serves charts on http://localhost:8000
- Access charts at http://localhost:8000/benchmark_chart.html
- Press Ctrl+C to stop

**Use case**: Live development - see chart updates immediately as you modify data.

## Data Structure

### Top-level Schema
```json
{
  "lastUpdated": "YYYY-MM-DD",
  "dataQualityNote": "string",
  "results": [/* array of result objects */],
  "pendingVerification": [/* array of unverified claims */],
  "speedBenchmarks": {}
}
```

### Result Object Schema
Each entry in the `results` array contains:
- `model`: Model name/identifier
- `dataset`: Benchmark dataset name
- `metric`: Metric type (accuracy, auroc, f1, composite, etc.)
- `value`: Numeric benchmark score
- `source`: Source identifier (e.g., "alphaxiv-leaderboard", "openai-blog")
- `sourceUrl`: URL to the source
- `accessDate`: Date accessed (YYYY-MM-DD format)
- `notes`: Optional additional context
- `verified`: Optional boolean flag for verified results
- `verifiedBy`: Optional verification source

### Pending Verification Schema
Entries in `pendingVerification` contain:
- `model`, `dataset`, `metric`, `source`, `sourceUrl`
- `claimedValue`: The claimed benchmark score
- `status`: Verification status (e.g., "needs-pdf-verification")
- `notes`: Context about what needs verification

## Working with the Data

### Query Examples Using jq

```bash
# Count total results
jq '.results | length' data/benchmarks.json

# Get all unique datasets
jq -r '.results[].dataset' data/benchmarks.json | sort -u

# Get all unique metrics
jq -r '.results[].metric' data/benchmarks.json | sort -u

# Find results for a specific model
jq '.results[] | select(.model == "gpt-4o")' data/benchmarks.json

# Find results for a specific dataset
jq '.results[] | select(.dataset == "imagenet-1k")' data/benchmarks.json

# Get top 5 models by value for a specific dataset/metric
jq '.results[] | select(.dataset == "imagenet-1k" and .metric == "top-1-accuracy") | {model, value}' data/benchmarks.json | jq -s 'sort_by(-.value) | .[0:5]'

# Count pending verifications
jq '.pendingVerification | length' data/benchmarks.json

# View specific result by index
jq '.results[0]' data/benchmarks.json

# Get verification status summary
jq '[.results[] | select(.verified == true)] | length' data/benchmarks.json

# Coding benchmark specific queries
# Get all HumanEval results sorted by score
jq '.results[] | select(.dataset == "humaneval") | {model, value, accessDate}' data/benchmarks.json | jq -s 'sort_by(-.value)'

# Get all SWE-Bench-Verified results (both verified and pending)
jq '.results[] | select(.dataset == "swe-bench-verified")' data/benchmarks.json
jq '.pendingVerification[] | select(.dataset == "swe-bench-verified")' data/benchmarks.json

# Compare a model across all coding benchmarks
jq '.results[] | select(.model == "claude-35-sonnet" and (.dataset == "humaneval" or .dataset == "mbpp" or .dataset == "swe-bench-verified")) | {dataset, metric, value}' data/benchmarks.json

# Count entries by dataset
jq '[.results[] | .dataset] | group_by(.) | map({dataset: .[0], count: length})' data/benchmarks.json
```

## Data Quality Notes

- The file is currently ~100KB with 286 benchmark results and 36 pending verifications
- Results are sourced from AlphaXiv leaderboards, published papers, and official model releases
- Verified results include a `verified` boolean and `verifiedBy` field
- Speed benchmarks require independent verification (noted in `dataQualityNote`)
- **Data recency**: Most entries are very recent (mid-to-late December 2025)
  - Coding benchmarks (HumanEval, MBPP, SWE-Bench) all added Dec 17-24, 2025
  - This appears to be an actively maintained, recently created dataset
- **SWE-Bench-Verified note**: Most results are in `pendingVerification` and use "accuracy" metric, while verified results use "resolve-rate" metric - these may represent different evaluation methodologies

## Typical Operations

When working with this file:
1. **Adding new results**: Append to the `results` array following the schema above
2. **Updating existing results**: Search by model+dataset+metric combination
3. **Verifying pending results**: Move from `pendingVerification` to `results` with verification fields
4. **Querying data**: Use `jq` for filtering and analysis (see examples above)
5. **Validating changes**: Check JSON syntax with `jq '.' data/benchmarks.json`

## OpenAI Model Benchmarks

### gpt-benchmarks-2025.json
Contains OpenAI-specific benchmark data organized by release date:
- GPT-4.5 (02-27-2025): SWE-Bench Verified 38.0%, SWE-Lancer Diamond 32.6%
- o3/o4-mini (04-16-2025): SWE-Bench Verified 71.7%
- GPT-5 (08-07-2025): SWE-Bench Verified 74.9%
- GPT-5.1 (11-13-2025): SWE-Bench Verified 76.3%
- GPT-5.2 Thinking (12-11-2025): SWE-Bench Verified 80.0%, SWE-Bench Pro 55.6%, SWE-Lancer IC Diamond 74.6%

### gpt-benchmarks-sources.txt
Lists official OpenAI blog post URLs for verification:
- All links follow pattern: `https://openai.com/index/introducing-{model-name}/`
- Used for fact-checking and citation purposes

### Query Examples
```bash
# Extract all GPT model benchmarks
jq '.' data/gpt-benchmarks-2025.json

# Get specific model's benchmarks
jq '."12-11-2025"' data/gpt-benchmarks-2025.json

# List all source URLs
cat data/gpt-benchmarks-sources.txt
```

## HumanEval Historical Dataset

### humaneval_benchmarks.json
Contains historical HumanEval pass@1 scores from 2021-2025:
- **Date Range**: July 2021 (Codex release) to January 2025
- **Total Data Points**: 15 historical benchmarks
- **Vendors Tracked**: OpenAI, Anthropic, DeepSeek
- **Metric**: pass@1 (percentage of problems solved on first attempt)

**Structure:**
```json
{
  "lastUpdated": "2025-01-14",
  "benchmark": "HumanEval",
  "metric": "pass@1",
  "description": "...",
  "results": [
    {
      "date": "YYYY-MM-DD",
      "model": "model-name",
      "vendor": "vendor-name",
      "value": 92.4,
      "source": "source-identifier",
      "sourceUrl": "https://...",
      "notes": "optional context"
    }
  ]
}
```

### Query Examples
```bash
# View all HumanEval historical data
jq '.results' data/humaneval_benchmarks.json

# Get top 5 scores
jq '.results | sort_by(-.value) | .[0:5]' data/humaneval_benchmarks.json

# Filter by vendor
jq '.results[] | select(.vendor == "OpenAI")' data/humaneval_benchmarks.json

# Get scores by year
jq '.results[] | select(.date | startswith("2024"))' data/humaneval_benchmarks.json

# Calculate average score by vendor
jq 'group_by(.vendor) | map({vendor: .[0].vendor, avg_score: (map(.value) | add / length)})' data/humaneval_benchmarks.json
```
