import sqlite3, os.path

x = os.path.isfile("StoryBase.db")

connect = sqlite3.connect("StoryBase.db")
curs = connect.cursor()

q = """
CREATE TABLE Login(
   Username TEXT,
   Password TEXT
);"""
curs.execute(q)
connect.commit()
q = """CREATE TABLE Stories(
   Content TEXT, 
   Name TEXT,
   Username TEXT,
   ID REAL,
   Date TEXT
);"""
curs.execute(q)
connect.commit()
q = """insert into Stories values ("Once upon a thyme","Untitled","Mokrejs",0,"October 15th");"""
curs.execute(q)
connect.commit()
q = """CREATE TABLE comments(storyID REAL,
   CContent TEXT,
   Date TEXT
);
"""
curs.execute(q)
connect.commit()
q = """CREATE TABLE StoryID(storyID REAL);
"""
curs.execute(q)
connect.commit()
