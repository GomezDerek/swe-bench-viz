import pandas as pd
import plotly.graph_objects as go

# ---- Step 1: Load the CSV file ----
csv_file = "data/AI_benchmarks_2025.csv"
df = pd.read_csv(csv_file)

# Convert 'date' to datetime format
df['date'] = pd.to_datetime(df['date'], format="%m-%d-%Y")
df = df.sort_values('date')

# ---- Step 2: Plot SWE-Bench Verified Trend ----
fig = go.Figure()

vendors = df['vendor'].unique()
colors = {"OpenAI":"#16ac86","Anthropic":"#d97757","Google":"#3b8cff","xAI":"#000000","DeepSeek":"#4763d5"}

for vendor in vendors:
    vendor_df = df[df['vendor']==vendor]
    fig.add_trace(go.Scatter(
        x=vendor_df['date'],
        y=vendor_df['swe_bench_verified'],
        mode='lines+markers',
        name=vendor,
        line=dict(color=colors[vendor], width=3),
        marker=dict(size=8),
        text=vendor_df['model'],
        # Individual hover tooltip (disabled for unified mode):
        hovertemplate='<b>%{text}</b><br>Date: %{x|%b %d, %Y}<br>Score: %{y}<extra></extra>'
    ))

# ---- Step 3: Update layout ----
fig.update_layout(
    title="The AI Coding Race (2025)",
    xaxis_title="Date",
    yaxis_title="SWE-Bench Verified Score",
    xaxis=dict(showgrid=True, hoverformat="%b %d, %Y"),
    yaxis=dict(showgrid=True, range=[35,85], ticksuffix="%"),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="center",
        x=0.5
    ),
    hoverlabel=dict(
        font_color="white"
        # font_color="black"
    ),
    template="plotly_white",
    # hovermode="x"
    # hovermode="x unified"
)

# ---- Step 5: Save and show figure ----
fig.write_html("chart.html")
fig.show()

