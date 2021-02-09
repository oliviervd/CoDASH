import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from components.viz import prov_timeline, prov_method, prov_method_time

layout = html.Div([
    dbc.Row([
        dbc.Col(
            html.H1(""), width={"size": 4, "offset": 1}  # create breathing space on top.
        )
    ]),
    dbc.Row([
        dbc.Col([
            html.H1("CoDASH")],
            width={"size": 4, "offset": 1}
        ),
        dbc.Col([
            dbc.ButtonGroup(
                [dbc.Button("HOME", href="/"),
                 dbc.Button("REGISTRATION", href="/registration"),
                 dbc.Button("PROVENANCE", href="/provenance")],
                size="lg"
            )
        ])
    ]),

    dbc.Row(
        dbc.Col(
            html.P("Objects can be collected in many different ways, the transferal from an object to the museum or "
                   "archive makes part of its provenance. This dashboard offers a glimps on when and how objects are "
                   "acquired."),
            width={"size": 4, "offset": 1}
        )
    ),

    dbc.Row([
        dbc.Col(
            dcc.Graph(
                id="provcount",
                figure=prov_timeline(),
                config={'displayModeBar': False}
            ), width={"size": 10, "offset": 1}
        )
    ]),
    # dbc.Row(
    #     dbc.Col(
    #         dcc.Graph(
    #             id="provmethod",
    #             figure=prov_method(),
    #             config={'displayModeBar': False}
    #         ), width={"size":10, "offset":1}
    #     )
    # ),

    dbc.Row([
        dbc.Col(width={"size": 1}),
        dbc.Col(
            dcc.Graph(
                id="provmethodtime",
                figure=prov_method_time("Design Museum Gent"),
                config={'displayModeBar': False}
            ), width={"size": 5}
        ),
        dbc.Col(
            dcc.Graph(
                id="provmethodtime",
                figure=prov_method_time("STAM"),
                config={'displayModeBar': False},
            ), width={"size": 5}
        )
    ])
])
