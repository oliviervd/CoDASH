# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

from utils import *

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

app.layout = html.Div(children=[
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

if __name__ == '__main__':
    app.run_server(debug=True)