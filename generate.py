import sqlite3, os.path

x = os.path.isfile("StoryBase.db")

if x:
   connect = sqlite3.connect("StoryBase.db")
   curs = connect.cursor()
   List = ["""
   CREATE TABLE Login(
      Username TEXT,
      Password TEXT
   );""","""CREATE TABLE Stories(
      Content TEXT, 
      Name TEXT,
      Username TEXT,
      ID REAL,
      Date TEXT
   );""","""CREATE TABLE comments(storyID REAL,
      CContent TEXT,
      Date TEXT
   );
   ""","""CREATE TABLE StoryID(storyID REAL);
   """]
   for q in List:
      curs.execute(q)
      connect.commit()
