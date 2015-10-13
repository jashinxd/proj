import sqlite3

def register(username,password):
    conn = sqlite3.connect("StoryBase.db")
    c = conn.cursor()
    q = """insert into Login values (""" + username + "," + password + """);"""
    c.execute(q)
    
def comment(storyID, CContent, Date):
    conn = sqlite3.connect("StoryBase.db")
    c = conn.cursor()
    q = """insert into comments values (""" + storyID + "," + CContent + "," + Date + """);"""
    c.execute(q)
    
def addStory(Content, Name, Username, ID, Date):
    conn = sqlite3.connect("StoryBase.db")
    c = conn.cursor()
    q = """insert into Stories values (""" + Content + "," + Name + "," + Username + "," +  ID + "," +  Date + """);"""
    c.execute(q)

