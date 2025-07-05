import dash
from dash import dcc, html
import pandas as pd
import plotly.graph_objs as go

# Load data
df = pd.read_csv("ozone_no2_data.csv")
df["datetime"] = pd.to_datetime(df["datetime"])

# Create the app
app = dash.Dash(__name__)
app.title = "Air Quality Trends"

# Layout
app.layout = html.Div([
    html.H1("Ground-Level Ozone and NO₂ Trends", style={"textAlign": "center"}),

    dcc.Graph(
        id="line-chart",
        figure={
            "data": [
                go.Scatter(
                    x=df["datetime"],
                    y=df["o3"],
                    mode="lines",
                    name="Ozone (O₃)",
                    line=dict(color="orange")
                ),
                go.Scatter(
                    x=df["datetime"],
                    y=df["no2"],
                    mode="lines",
                    name="Nitrogen Dioxide (NO₂)",
                    line=dict(color="blue")
                )
            ],
            "layout": go.Layout(
                title="Daily Pollutant Concentrations Over Time",
                xaxis={"title": "Date"},
                yaxis={"title": "Concentration (µg/m³ or ppb)"},
                hovermode="x unified"
            )
        }
    )
])

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))
    app.run(host="0.0.0.0", port=port)
