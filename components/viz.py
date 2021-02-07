import plotly.express as px
import numpy as np
import plotly.graph_objects as go

from components.data_prep import *
from components.utils import count_list
from plotly.subplots import make_subplots


def data_completeness():
    cnt_all = counter_reg()

    fig = make_subplots(rows=1, cols=2, specs=[[{}, {}]], shared_xaxes=True,
                        shared_yaxes=False, vertical_spacing=0.001)

    # STAM
    fig.append_trace(go.Bar(
        x=cnt_all["STAM"],
        y=cnt_all.index,
        text=cnt_all["STAM_P"],
        marker=dict(
            color='rgba(50, 171, 96, 0.6)',
            line=dict(
                color='rgba(50, 171, 96, 1.0)',
                width=1),
        ),
        name='STAM',
        orientation='h'
    ), 1, 1)

    # DMG
    fig.append_trace(go.Bar(
        x=cnt_all["DMG"],
        y=cnt_all.index,
        text=cnt_all["DMG_P"],
        marker=dict(
            color='rgba(90, 160, 96, 0.6)',
            line=dict(
                color='rgba(50, 171, 96, 1.0)',
                width=1),
        ),
        name='Design Museum Gent',
        orientation='h'
    ), 1, 2)

    fig.update_layout(
        title="overview of data completeness based on CoGhent data model",
        yaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=True,
            domain=[0, 0.85],
        ),

        yaxis2=dict(
            showgrid=False,
            showline=False,
            showticklabels=True,
            domain=[0, 0.85]
        ),

        xaxis=dict(
            zeroline=False,
            showline=False,
            showticklabels=True,
            showgrid=True,
            domain=[0, 0.45]
        ),

        xaxis2=dict(
            zeroline=False,
            showline=False,
            showticklabels=True,
            showgrid=True,
            domain=[0.55, 1]
        ),
        legend=dict(x=0.029, y=1.038, font_size=10),
        margin=dict(l=100, r=20, t=70, b=70),
        paper_bgcolor='rgb(248, 248, 255)',
        plot_bgcolor='rgb(248, 248, 255)',
    )

    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')

    return fig


def upload_sched():
    cnt = fetch_count_history()
    fig = px.line(cnt, x=cnt.index, y="totalcount", color="institution")
    fig.update_xaxes(title_text="")
    fig.update_yaxes(title_text="number of objects published in LDES")
    return fig


def prov_timeline():
    prov = fetch_prov_info()
    fig = px.histogram(prov, "start", color="inst")
    fig.update_xaxes(title_text="date of transfer")
    fig.update_yaxes(title_text="number of objects transferred on given date")
    fig.update_layout(title="overview of object transfers (acquisitions, gifts, ...) based on time of transfer")
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ),legend_title_text="", xaxis_title="")
    return fig


def prov_method():
    prov = fetch_prov_info()
    fig = px.histogram(prov, y="method", color="inst")
    fig.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    ))
    return fig


def prov_method_time(inst):
    prov = fetch_prov_info()
    prov = prov[prov["inst"] == inst]
    # prov["start"] = pd.to_datetime(prov["start"], yearfirst=True)
    # prov["end"] = pd.to_datetime(prov["end"], yearfirst=True)
    fig = px.histogram(prov, "start", color="method",
                       title="{}".format(inst))
    # fig.update_yaxes(title="number of objects transferred on a given date grouped by method")
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ),legend_title_text="", xaxis_title="")
    fig.update_yaxes(visible=True, title="number of objects received")
    return fig


def prov_method_time_all():
    prov = fetch_prov_info()
    # prov["start"] = pd.to_datetime(prov["start"], yearfirst=True)
    # prov["end"] = pd.to_datetime(prov["end"], yearfirst=True)
    fig = px.histogram(prov, "start", color="method", facet_col="inst")
    # fig.update_yaxes(title="number of objects transferred on a given date grouped by method")
    fig.update_yaxes(matches=None)
    fig.update_xaxes(matches=None)
    return fig


