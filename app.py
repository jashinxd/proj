from flask import Flask, render_template, request, redirect, url_for
import authen
import Append

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
                        return redirect(url_for("storypage"))
                else:
                        error = "Your Username or Password is incorrect. Please try again."
                        return render_template("login.html", problem = error )
	
@app.route("/storypage")
def storypage():
    q="""
    SELECT *
    FROM Stories
    """
    conn = sqlite3.connect("StoryBase.db")
    c = conn.cursor()
    result = c.execute(q)
    return render_template("storypage.html", result=result)

if (__name__ == "__main__"):
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
