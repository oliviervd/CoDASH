from components.utils import *
from components.viz import data_completeness, upload_sched, prov_timeline
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

layout = html.Div([
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
                [dbc.Button("HOME",href="/"),
                 dbc.Button("REGISTRATION", href="/registration"),
                 dbc.Button("PROVENANCE", href="/provenance")],
                size="lg"
            )
        ])
    ], justify="end",),

    dbc.Row(
        dbc.Col(
            html.P("Collections of Ghent will publish  a minimum of 100.000 cultural heritage "
                   "objects from a range of five cultural heritage institutions based in Ghent. "
                   "This data will be made accessible as Linked Open Data via our Linked Data Event Stream (LDES). "
                   "CoDASH analyzes this data and translates it into human readable graphs, "
                   "offering insights into the collections at large. This dashboard is structered in different "
                   "thematic groups that can be accessed via the tabs on top."),
            width={"size": 4, "offset": 1}
        )
    ),

    dbc.Row(
        dbc.Col(
            dcc.Graph(
                id="sched",
                figure=upload_sched(),
                config={'displayModeBar': False}
            ), width={"size": 10, "offset": 1}
        )
    ),

    dbc.Row(
        dbc.Col(
            html.Div('''last update: ''' + str(datetime.now())),
            width={"size": 10, "offset": 1}
        )
    ),

])
