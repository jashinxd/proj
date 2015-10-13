import sqlite3

def authenticate(username,password):
    conn = sqlite3.connect("StoryBase.db")
    c = conn.cursor()
    q = """
    SELECT Login.Username, Login.Password
    FROM Login
    WHERE Login.Username = """ + username
    result = c.execute(q)
    for r in result:
        if r[1] == password:
            return True
    return False

