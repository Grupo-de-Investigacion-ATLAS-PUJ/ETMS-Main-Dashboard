# /business_logic/business_logic.py

import plotly.graph_objs as go
import pandas as pd
import numpy as np
from dash.dependencies import Input, Output
from data.data_service import query_data  # Import data service

def register_callbacks(app):
    # Callback to update the performance graph dynamically
    @app.callback(
        Output('performance-graph', 'figure'),
        [Input('interval-component', 'n_intervals')]
    )
    def update_performance_graph(n):
        df = query_data()

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=pd.to_datetime(df['time']),
                                 y=df['original_value_float'],
                                 mode='lines+markers',
                                 name='Performance'))
        fig.update_layout(title='System Performance',
                          xaxis_title='Time',
                          yaxis_title='Value')

        return fig

    # Callback to update the trend graph dynamically
    @app.callback(
        Output('trend-graph', 'figure'),
        [Input('interval-component', 'n_intervals')]
    )
    def update_trend_graph(n):
        df = query_data()

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=pd.to_datetime(df['time']),
                                 y=df['original_value_float'],
                                 mode='lines',
                                 name='Trend'))

        z = pd.to_datetime(df['time']).astype(int) // 10**9  # Convert time to seconds
        p = np.polyfit(z, df['original_value_float'], 1)
        fig.add_trace(go.Scatter(x=pd.to_datetime(df['time']),
                                 y=np.polyval(p, z),
                                 mode='lines',
                                 name='Trendline'))

        fig.update_layout(title='Trend Analysis',
                          xaxis_title='Time',
                          yaxis_title='Value')

        return fig

    # More callbacks go here...

