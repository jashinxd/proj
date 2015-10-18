from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import authen
import Append
import datetime

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html")

@app.route("/register", methods=["POST","GET"])
def register():
        if (request.method == "GET"):
                return render_template("register.html")
        else:
                username = request.form["username"]
                password = request.form["password"]
                Append.register(username,password)
                return redirect(url_for("login"))

@app.route("/login", methods = ["POST", "GET"])
def login():
	if (request.method == "GET"):
		return render_template("login.html")
	else:
		username = request.form["username"]
		password = request.form["password"]
                if (authen.authenticate(username, password)):
                        session['n']=username
                        return redirect(url_for("storypage"))
                else:
                        error = "Your Username or Password is incorrect. Please try again."
                        return render_template("login.html", problem = error )
	
@app.route("/storypage", methods=["POST","GET"])
def storypage():
    if (request.method == "POST"):
        Append.comment(request.form["button"],request.form["comment"],datetime.date.today().strftime("%B %d, %Y"))
    q="""
    SELECT *
    FROM Stories
    """
    conn = sqlite3.connect("StoryBase.db")
    c = conn.cursor()
    result = c.execute(q)
    MainHTML = ""
    for r in result:
    	StoryHTML = """
        <h3> %s<br> by %s <br> on %s</h3>
        <p>
    	%s
        </p>
        <hr>
        <form method="POST">
        Comment: <input type="text" name="comment">
        <input type="submit" name="button" value=%s>
        </form>
        Comments: <br><hr>""" % (r[1],r[2],r[4],r[0],r[3])
    	q="""
        SELECT *
    	FROM comments where storyID = %s
    	""" % (r[3])
    	comments = c.execute(q)
    	for c in comments:
    		commentHTML = """
    		%s on %s
                <hr>
                """ % (c[1],c[2])
    		StoryHTML = StoryHTML + commentHTML
        MainHTML = MainHTML + StoryHTML
        
    return render_template("storypage.html", result=MainHTML)

@app.route("/addStory",methods=["GET","POST"])
def addStory():
        conn = sqlite3.connect("StoryBase.db")
        c = conn.cursor()
        if (request.method=="GET"):
                return render_template("addStory.html")
        else:
                Story = request.form["Story"]
                Title = request.form["Title"]
                q = """SELECT *
                FROM StoryID
                """
                ID = c.execute(q)
                Append.addStory(Story,Title,session['n'],1,datetime.date.today().strftime("%B %d, %Y"))
                return redirect(url_for("storypage"))

if (__name__ == "__main__"):
        app.debug = True
        app.secret_key = "secret"
        app.run(host='0.0.0.0', port=8000)
