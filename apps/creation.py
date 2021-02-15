from components.utils import *
from components.viz import creators_count
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

layout =  html.Div([
    dbc.Row([
        dbc.Col(
            html.H1(""), width={"size": 4, "offset": 1}  # create breathing space on top.
        )
   ]),
    dbc.Row([
        dbc.Col(
            html.H1("CoDASH"), width={"size": 4, "offset": 1}
        ),
        dbc.Col([
            dbc.ButtonGroup(
                [dbc.Button("HOME", href="/"),
                 dbc.Button("CREATION", href="/creation"),
                 dbc.Button("REGISTRATION", href="/registration"),
                 dbc.Button("PROVENANCE", href="/provenance")],
                size="lg"
            )
        ])
    ]),
    dbc.Row([
        dbc.Col(
            dcc.Graph(
                id="c_count",
                figure=creators_count()
            )
        )
    ])
])