from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from include import userLogin
import secrets



app = Flask(__name__)

app.config["TEMPLATE_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



@app.route("/", methods=['GET', 'POST'])
def chat():
    if not session.get("homeserver"):
        return redirect("/login")
    else:
        userLogin.clientLogin()
        return render_template("index.html")



@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")

    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        homeserver = request.form.get("homeserver")

        if homeserver == "other":
            homeserver = request.form.get("newHomeServer")

        homeserver = homeserver if homeserver.startswith("https://") or homeserver.startswith("http://") else "https://"+homeserver

        response = userLogin.clientLogin(username, password, homeserver)
        
        if hasattr(response, 'message'):
            return render_template("login.html", response=response.message)
        else:
            print(response.access_token)
            session["homeserver"] = homeserver
            session["user_id"] = username
            session["device_id"] = response.device_id
            session["access_token"] = response.access_token
            return redirect('/')



@app.route("/logout")
def logout():
    userLogin.clientLogin(checkLogout=True)
    session.clear()
    return redirect('/')