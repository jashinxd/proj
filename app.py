from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
	if (request.method == "GET"):
		return render_template("login.html")
	else:
		username = request.form["username"]
		password = request.form["password"]
		
		#Authenticate, do something
		return render_template("login.html") + "Username entered: " + username + "<br> Password entered:" + password		

if (__name__ == "__main__"):
    app.debug = True
    app.run(host='0.0.0.0', port=8000)