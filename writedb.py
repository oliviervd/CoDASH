# generates a table and updates it with changes over time
import sqlite3
from utils import *

conn = sqlite3.connect("tracker.db")
c = conn.cursor()

def update_tracker():
    conn = sqlite3.connect("tracker.db")
    c = conn.cursor()
    c = conn.cursor()
    for i in count_list:
        format_str = """INSERT INTO totalcount (totalcount, date, institution) VALUES ("{count}","{date}","{inst}")"""
        sql_command = format_str.format(count=i[0], date=i[1], inst=i[2])
        c.execute(sql_command)
    conn.commit()
    conn.close()

update_tracker()
