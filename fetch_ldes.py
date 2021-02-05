import sqlite3
conn = sqlite3.connect("/Users/huynslol/IdeaProjects/adlib2eventstream/eventstream.db")
c = conn.cursor()

c.execute('SELECT payload FROM Members')
db = c.fetchall()


