import sqlite3

conn = sqlite3.connect("StoryBase.db")
c = conn.cursor()

q = """
SELECT Login.Username, Login.Password
FROM Login
"""
result = c.execute(q)

def authenticate(username,password):
    q = """
    SELECT Login.Username, Login.Password
    FROM Login
    WHERE Login.Username = """ + username + """ and Login.Password = """ + password
    result = c.execute(q)
    if result.size() > 0:
        return True
    else:
        return False

