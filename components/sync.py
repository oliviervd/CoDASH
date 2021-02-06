from datetime import datetime
from threading import Timer
import subprocess
import sqlite3
import json

from components.data_prep import *
from components.utils import *
from components.utils import sql_to_dataframe

x = datetime.today()
y = x.replace(day=x.day + 1, hour=1, minute=0, second=0, microsecond=0)
delta_t = y - x

secs = delta_t.seconds + 1


def sync():
    # sync with adlib2eventstream > fetch latest objects from LDES
    subprocess.run('node /Users/huynslol/IdeaProjects/adlib2eventstream/bin/adlib2backend.js', shell=True)

    # copy to db
    sql_to_dataframe()

    # update counter
    # total_count()

    # append new count and timestamp to db

    df_all = sql_to_dataframe()

    stam_obj = list(
        filter(lambda objet: objet["MaterieelDing.beheerder"] == 'http://www.wikidata.org/entity/Q980285', df_all))
    dmg_obj = list(
        filter(lambda objet: objet["MaterieelDing.beheerder"] == 'http://www.wikidata.org/entity/Q1809071', df_all))

    count_list = [(int(len(stam_obj)), current_time(), "STAM"),
                  (int(len(dmg_obj)), current_time(), "Design Museum Gent")]

    conn_2 = sqlite3.connect("../data/tracker.db")
    c2 = conn_2.cursor()
    for i in count_list:
        format_str = """INSERT INTO totalcount (totalcount, date, institution) VALUES ("{count}","{date}","{inst}")"""
        sql_command = format_str.format(count=i[0], date=i[1], inst=i[2])
        c2.execute(sql_command)
    conn_2.commit()
    conn_2.close()

t = Timer(secs, sync)
t.start()
