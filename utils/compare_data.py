#!/usr/bin/env python3
"""
Compare data points between AI_benchmarks_2025.csv and benchmarks.json
"""
import pandas as pd
import json
from pathlib import Path

# Get the directory containing this script
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
DATA_DIR = PROJECT_ROOT / 'data'

# Load CSV data
csv_df = pd.read_csv(DATA_DIR / 'AI_benchmarks_2025.csv')
csv_df = csv_df.dropna(subset=['swe_bench_verified'])

# Load JSON data
with open(DATA_DIR / 'benchmarks.json', 'r') as f:
    json_data = json.load(f)

# Extract SWE-Bench Verified entries from JSON
verified = [r for r in json_data['results'] if r['dataset'] == 'swe-bench-verified']
pending = [r for r in json_data['pendingVerification'] if r['dataset'] == 'swe-bench-verified']

print("=== CSV Data (12 entries) ===")
for idx, row in csv_df.iterrows():
    print(f"{row['model']}: {row['swe_bench_verified']}%")

print("\n=== JSON Verified Results (3 entries) ===")
for entry in verified:
    print(f"{entry['model']}: {entry['value']}%")

print("\n=== JSON Pending Verification (8 entries) ===")
for entry in pending:
    claimed = entry.get('claimedValue', 'null')
    print(f"{entry['model']}: {claimed}")

# Try to find matches
print("\n=== Potential Matches ===")
csv_models = csv_df['model'].str.lower().str.replace(' ', '-').str.replace('/', '').tolist()
json_models_verified = [r['model'].lower() for r in verified]
json_models_pending = [r['model'].lower() for r in pending]

matches_verified = []
matches_pending = []

for idx, row in csv_df.iterrows():
    csv_model = row['model']
    csv_normalized = csv_model.lower().replace(' ', '-').replace('/', '')

    # Check verified
    for j_entry in verified:
        j_model_normalized = j_entry['model'].lower()
        if csv_normalized in j_model_normalized or j_model_normalized in csv_normalized:
            matches_verified.append({
                'csv_model': csv_model,
                'json_model': j_entry['model'],
                'csv_value': row['swe_bench_verified'],
                'json_value': j_entry['value']
            })

    # Check pending
    for j_entry in pending:
        j_model_normalized = j_entry['model'].lower()
        # Try various matching strategies
        if ('claude-3.7' in j_model_normalized and 'claude 3.7' in csv_model.lower()) or \
           ('opus-4.5' in j_model_normalized and 'opus 4.5' in csv_model.lower()) or \
           ('sonnet-4' in j_model_normalized and 'sonnet 4.5' in csv_model.lower()) or \
           ('o3' == j_model_normalized and 'o3' in csv_model.lower()):
            matches_pending.append({
                'csv_model': csv_model,
                'json_model': j_entry['model'],
                'csv_value': row['swe_bench_verified'],
                'json_claimed': j_entry.get('claimedValue', 'null')
            })

print("\nMatches in Verified Results:")
if matches_verified:
    for m in matches_verified:
        print(f"  {m['csv_model']} ({m['csv_value']}%) ~ {m['json_model']} ({m['json_value']}%)")
else:
    print("  None")

print("\nMatches in Pending Verification:")
if matches_pending:
    for m in matches_pending:
        print(f"  {m['csv_model']} ({m['csv_value']}%) ~ {m['json_model']} (claimed: {m['json_claimed']})")
else:
    print("  None")

print(f"\n=== Summary ===")
print(f"CSV entries: {len(csv_df)}")
print(f"JSON verified: {len(verified)}")
print(f"JSON pending: {len(pending)}")
print(f"Potential matches (verified): {len(matches_verified)}")
print(f"Potential matches (pending): {len(matches_pending)}")
print(f"Total potential overlaps: {len(matches_verified) + len(matches_pending)}")
