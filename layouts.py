import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import dash_table

###################### HOME Layout ######################

layout_home = html.Div(children=[
    html.H1(children="CoDASH"),

    html.Div(children='''
        total number of objects published on the LDES: ''' + str(total_count())),
    html.Div(children='''
        number of objects published by STAM: ''' + str(len(stam_obj))),
    html.Div(children='''
        number of objects published by Design Museum Gent: ''' + str(len(dmg_obj))),
    html.Div(children='''
        last update: ''' + str(datetime.now())),

    dcc.Graph(
        id='counter',
        figure= counter_fig
    )
])