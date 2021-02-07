import json
import requests
from datetime import datetime
from collections import Counter
import sqlite3
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go


def sql_to_json():
    conn_1 = sqlite3.connect("data/eventstream.db")
    c1 = conn_1.cursor()
    c1.execute("SELECT payload FROM Members")
    db = c1.fetchall()

    df_all = []
    for i in db:
        obj = json.loads(i[0])
        df_all.append(obj)

    return df_all


def current_time():
    now = datetime.now()
    return now.strftime("%y-%m-%d")


def update_tracker():
    """appends new count and timestamp to db"""
    pass


df_all = sql_to_json()

stam_obj = list(
    filter(lambda objet: objet["MaterieelDing.beheerder"] == 'http://www.wikidata.org/entity/Q980285', df_all))
dmg_obj = list(
    filter(lambda objet: objet["MaterieelDing.beheerder"] == 'http://www.wikidata.org/entity/Q1809071', df_all))

count_list = [(int(len(stam_obj)), current_time(), "STAM"),
              (int(len(dmg_obj)), current_time(), "Design Museum Gent")]
