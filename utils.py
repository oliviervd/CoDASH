import json
from fetch_ldes import *
import requests
from datetime import datetime
from collections import Counter
import sqlite3
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

# transform db to list of dicts
all = []
for i in db:
    obj = json.loads(i[0])
    all.append(obj)

def current_time():
    now = datetime.now()
    return now.strftime("%y-%m-%d")


def total_count():
    """counts all objects in the db"""
    return len(all)

def count_tracker():
    """appends new count and timestamp to db"""
    pass




stam_obj = list(
    filter(lambda object: object["MaterieelDing.beheerder"] == 'http://www.wikidata.org/entity/Q980285', all))
dmg_obj = list(
    filter(lambda object: object["MaterieelDing.beheerder"] == 'http://www.wikidata.org/entity/Q1809071', all))

count_list = [(int(len(stam_obj)), current_time(), "STAM"),
              (int(len(dmg_obj)), current_time(), "Design Museum Gent")]

conn_count = sqlite3.connect("tracker.db")
c_count = conn_count.cursor()
df_count = pd.read_sql_query("SELECT * FROM totalcount", conn_count)

df_count["totalcount"] = df_count["totalcount"].astype(int)

counter_fig = px.line(df_count, x="date", y="totalcount", color="institution")


