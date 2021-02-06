import json
import requests
from datetime import datetime
from collections import Counter
import sqlite3
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go


def sql_to_dataframe():
    conn_1 = sqlite3.connect("/Users/huynslol/IdeaProjects/adlib2eventstream/eventstream.db")
    c1 = conn_1.cursor()
    c1.execute("SELECT payload FROM Members")
    db = c1.fetchall()

    all = []
    for i in db:
        obj = json.loads(i[0])
        all.append(obj)

    return all


def current_time():
    now = datetime.now()
    return now.strftime("%y-%m-%d")


def update_tracker():
    """appends new count and timestamp to db"""
    pass

df_all = sql_to_dataframe()

stam_obj = list(
    filter(lambda objet: objet["MaterieelDing.beheerder"] == 'http://www.wikidata.org/entity/Q980285', df_all))
dmg_obj = list(
    filter(lambda objet: objet["MaterieelDing.beheerder"] == 'http://www.wikidata.org/entity/Q1809071', df_all))

count_list = [(int(len(stam_obj)), current_time(), "STAM"),
            (int(len(dmg_obj)), current_time(), "Design Museum Gent")]

# def update_sqlcount():
#     conn_2 = sqlite3.connect("/Users/huynslol/Documents/CoDASH/data/tracker.db")
#     c2 = conn_2.cursor()
#     for i in count_list:
#         format_str = """INSERT INTO totalcount (totalcount, date, institution) VALUES ("{count}","{date}","{inst}")"""
#         sql_command = format_str.format(count=i[0], date=i[1], inst=i[2])
#         c2.execute(sql_command)
#     conn_2.commit()
#     conn_2.close()



# conn_count = sqlite3.connect("/data/tracker.db")
# c_count = conn_count.cursor()
# df_count = pd.read_sql_query("SELECT * FROM totalcount", conn_count)
# df_count["totalcount"] = df_count["totalcount"].astype(int)
