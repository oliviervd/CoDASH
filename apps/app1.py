from components.utils import *
from components.viz import data_completeness, upload_sched, prov_timeline
import dash_core_components as dcc
import dash_html_components as html

layout = html.Div(children=[
    html.H1(children="CoDASH"),
    html.Div(children='''
        last update: ''' + str(datetime.now())),

    dcc.Graph(
        id="sched",
        figure=upload_sched()
    ),

    dcc.Graph(
        id="1",
        figure=data_completeness()
    ),

    dcc.Graph(
        id="provcount",
        figure = prov_timeline()
    )

])
