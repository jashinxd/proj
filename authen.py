import sqlite3

def authenticate(username,password):
    conn = sqlite3.connect("StoryBase.db")
    c = conn.cursor()
    q = """
    SELECT Username, Password
    FROM Login
    WHERE Login.Username = '%s'
    """ % username 
    result = c.execute(q)
    for r in result:
        if r[1] == password:
            return True
    return False

