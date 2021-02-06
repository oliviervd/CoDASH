from components.utils import *
from components.viz import data_completeness
import dash_core_components as dcc
import dash_html_components as html

layout = html.Div(children=[
    html.H1(children="CoDASH"),
    html.Div(children='''
        number of objects published by STAM: ''' + str(len(stam_obj))),
    html.Div(children='''
        number of objects published by Design Museum Gent: ''' + str(len(dmg_obj))),
    html.Div(children='''
        last update: ''' + str(datetime.now())),

    dcc.Graph(
        id="1",
        figure=data_completeness()
    ),

])
