# /presentation/layout.py

from dash import dcc, html

def create_layout():
    return html.Div([    
        html.Div([
            html.Img(src='/assets/ATLAS-Logo-White-transparent.png', style={'width': '100%', 'padding': '10px'}),
            html.H2("Menu", className="sidebar-header"),
            html.Ul([
                html.Li(html.A("Variables", href="#")),
                html.Li(html.A("Alerts", href="#")),
                html.Li(html.A("Reports", href="#")),
                html.Li(html.A("Dashboards", href="#")),
                html.Li(html.A("Users", href="#")),
                html.Li(html.A("Options", href="#"))
            ], className="sidebar-menu")
        ], className="sidebar"),

        html.Div([
            html.H1("Dashboard", className="dashboard-header"),
            dcc.Graph(id='performance-graph'),
            dcc.Graph(id='trend-graph'),
            dcc.Interval(id='interval-component', interval=5000, n_intervals=0),
            dcc.Graph(id='voltage-histogram'),
            dcc.Graph(id='moving-average-graph'),
            dcc.Graph(id='std-dev-graph'),
            dcc.Graph(id='min-max-graph'),
            dcc.Graph(id='cumulative-sum-graph'),
            dcc.Graph(id='rate-of-change-graph'),
            dcc.Graph(id='power-graph'),
            dcc.Graph(id='fft-graph')
        ], className="content")
    ])

