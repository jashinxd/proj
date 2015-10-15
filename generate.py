import sqlite3, os.path

x = os.path.isfile("StoryBase.db")

connect = sqlite3.connect("StoryBase.db")
curs = connect.cursor()

q = """
CREATE TABLE Login(
   Username TEXT,
   Password TEXT
);"""
#if not x:
curs.execute(q)
connect.commit()
q = """insert into Login values ("APCS","B");"""
#if not x:
curs.execute(q)
connect.commit()
q = """CREATE TABLE stories(
   Content TEXT, 
   Name TEXT,
   Username TEXT,
   ID REAL,
   Date TEXT
);"""
#if not x:
curs.execute(q)
connect.commit()
q = """CREATE TABLE comments(storyID REAL,
   CContent TEXT,
   Date TEXT
);
"""
#if not x:
#print q
curs.execute(q)
connect.commit()

