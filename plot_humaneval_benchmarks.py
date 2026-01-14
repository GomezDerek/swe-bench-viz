import json
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# ---- Step 1: Load the JSON file ----
json_file = "data/humaneval_benchmarks.json"
with open(json_file, 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data['results'])

# Convert 'date' to datetime format
df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d")
df = df.sort_values('date')

# ---- Step 2: Plot HumanEval Trend ----
fig = go.Figure()

# Use the same vendor colors as plot_ai_benchmarks.py
vendors = df['vendor'].unique()
colors = {
    "OpenAI": "#16ac86",
    "Anthropic": "#d97757",
    "Google": "#3b8cff",
    "xAI": "#000000",
    "DeepSeek": "#4763d5"
}

for vendor in vendors:
    vendor_df = df[df['vendor'] == vendor]
    fig.add_trace(go.Scatter(
        x=vendor_df['date'],
        y=vendor_df['value'],
        mode='lines+markers',
        name=vendor,
        line=dict(color=colors.get(vendor, '#999999'), width=3),
        marker=dict(size=8),
        text=vendor_df['model'],
        hovertemplate='<b>%{text}</b><br>Date: %{x|%b %d, %Y}<br>Score: %{y}<extra></extra>'
    ))

# ---- Step 3: Update layout ----
fig.update_layout(
    title="The AI Coding Race (2021-2025)",
    xaxis_title="Date",
    yaxis_title="HumanEval Pass@1 Score",
    xaxis=dict(showgrid=True, hoverformat="%b %d, %Y"),
    yaxis=dict(showgrid=True, range=[0, 100], ticksuffix="%"),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="center",
        x=0.5
    ),
    hoverlabel=dict(
        font_color="white"
    ),
    template="plotly_white",
    annotations=[
        dict(
            x=datetime(2021, 7, 15),
            y=28.8,
            text="HumanEval<br>Released",
            showarrow=True,
            arrowhead=2,
            ax=-40,
            ay=-40,
            font=dict(size=10, color="#666666"),
            bgcolor="rgba(255,255,255,0.8)",
            bordercolor="#cccccc",
            borderwidth=1
        )
    ]
)

# ---- Step 4: Save and show figure ----
fig.write_html("humaneval_chart.html")
print(f"Chart saved to humaneval_chart.html")
print(f"\nBenchmark: {data['benchmark']}")
print(f"Metric: {data['metric']}")
print(f"Total data points: {len(df)}")
print(f"Date range: {df['date'].min().strftime('%Y-%m-%d')} to {df['date'].max().strftime('%Y-%m-%d')}")
print(f"\nTop 3 scores:")
print(df.nlargest(3, 'value')[['date', 'model', 'vendor', 'value']].to_string(index=False))

fig.show()
