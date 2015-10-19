import sqlite3

def GreatestStoryID():
    conn = sqlite3.connect("StoryBase.db")
    c = conn.cursor()
    q="""SELECT * FROM Stories;
    	"""
    result = c.execute(q)
    x = 0
    for r in result:
        if r[3] > x:
            x = r[3]
    return x

def register(username,password):
    conn = sqlite3.connect("StoryBase.db")
    c = conn.cursor()
    q = """insert into Login values ('%s','%s');""" % (username,password)
    c.execute(q)
    conn.commit()
    
def comment(storyID, CContent, Date):
    conn = sqlite3.connect("StoryBase.db")
    c = conn.cursor()
    q = """insert into comments values ('%s','%s','%s');""" % (storyID, CContent, Date)
    c.execute(q)
    conn.commit()
    
def addStory(Content, Name, Username, ID, Date):
    conn = sqlite3.connect("StoryBase.db")
    c = conn.cursor()
    q = """insert into Stories values ('%s','%s','%s','%s','%s');""" % (Content,Name,Username,ID,Date)
    c.execute(q)
    conn.commit()

