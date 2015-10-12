import sqlite3

connect = sqlite3.connect("DOPESQL.db")
curs = connect.cursor()

q = """CREATE TABLE users(
   Username TEXT,
   Password TEXT,
);

INSERT INTO users VALUES (Sudo, potato);
INSERT INTO users VALUES (ThatOneGuy, thatonepassword);
INSERT INTO users VALUES (Example3, 123456);

CREATE TABLE stories(
   content TEXT, 
   name TEXT,
   Username TEXT,
   ID REAL,
   Date TEXT,
);

INSERT INTO stories VALUES (this is a story, Story1, ThatOneGuy, 0, October 12 2015);

CREATE TABLE comments(storyID REAL, CContent TEXT, Date TEXT);

INSERT INTO comments VALUES (0, this is a comment, October 12 2015);"""

curs.execute(q)
conn.commit()

