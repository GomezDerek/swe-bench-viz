# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains benchmark data for AI/ML models in multiple formats:

### Core Files
- **`benchmarks.json`** - Comprehensive database of 286 verified results + 36 pending verifications across multiple benchmark categories (last updated: 2025-12-21)
- **`AI_benchmarks_2025.csv`** - Timeline data tracking frontier model performance across 2025 (Feb-Dec)
- **`plot_ai_benchmarks.py`** - Python visualization script using pandas + plotly to chart benchmark trends
- **`requirements.txt`** - Python dependencies for visualization script
- **`gpt-benchmarks-2025.json`** - Focused collection of OpenAI model benchmarks (GPT-4.5 through GPT-5.2)
- **`gpt-benchmarks-sources.txt`** - Source URLs for OpenAI benchmark claims

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
- Color-coded by vendor: OpenAI (blue), Anthropic (green), Google (orange), xAI (purple)
- Opens automatically in default browser

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
jq '.results | length' benchmarks.json

# Get all unique datasets
jq -r '.results[].dataset' benchmarks.json | sort -u

# Get all unique metrics
jq -r '.results[].metric' benchmarks.json | sort -u

# Find results for a specific model
jq '.results[] | select(.model == "gpt-4o")' benchmarks.json

# Find results for a specific dataset
jq '.results[] | select(.dataset == "imagenet-1k")' benchmarks.json

# Get top 5 models by value for a specific dataset/metric
jq '.results[] | select(.dataset == "imagenet-1k" and .metric == "top-1-accuracy") | {model, value}' benchmarks.json | jq -s 'sort_by(-.value) | .[0:5]'

# Count pending verifications
jq '.pendingVerification | length' benchmarks.json

# View specific result by index
jq '.results[0]' benchmarks.json

# Get verification status summary
jq '[.results[] | select(.verified == true)] | length' benchmarks.json

# Coding benchmark specific queries
# Get all HumanEval results sorted by score
jq '.results[] | select(.dataset == "humaneval") | {model, value, accessDate}' benchmarks.json | jq -s 'sort_by(-.value)'

# Get all SWE-Bench-Verified results (both verified and pending)
jq '.results[] | select(.dataset == "swe-bench-verified")' benchmarks.json
jq '.pendingVerification[] | select(.dataset == "swe-bench-verified")' benchmarks.json

# Compare a model across all coding benchmarks
jq '.results[] | select(.model == "claude-35-sonnet" and (.dataset == "humaneval" or .dataset == "mbpp" or .dataset == "swe-bench-verified")) | {dataset, metric, value}' benchmarks.json

# Count entries by dataset
jq '[.results[] | .dataset] | group_by(.) | map({dataset: .[0], count: length})' benchmarks.json
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
5. **Validating changes**: Check JSON syntax with `jq '.' benchmarks.json`

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
jq '.' gpt-benchmarks-2025.json

# Get specific model's benchmarks
jq '."12-11-2025"' gpt-benchmarks-2025.json

# List all source URLs
cat gpt-benchmarks-sources.txt
```
