from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from include import userLogin
from include import utils as ut
import requests


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
        #userLogin.clientLogin()
        joins = ut.getJoinedRooms()
        userAvatar = ut.getAvatar(session['user_id']) if ut.getAvatar(session['user_id']) else 'static/img/default.png'
        return render_template("index.html", userAvatar=userAvatar, rooms=joins.json()['joined_rooms'])



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

        #response = userLogin.clientLogin(username, password, homeserver)

        try:
            clientRequest = {"type":"m.login.password","identifier":{"type":"m.id.user","user":username},"password":password}
            response = requests.post(f'{homeserver}/_matrix/client/r0/login', json=clientRequest)

        except:
            return render_template("login.html", response='A error has ocurred, check homeserver informations!')

        if response.status_code != 200:
            return render_template("login.html", response=response.json()['error'])
        else:
            session["homeserver"] = homeserver
            session["user_id"] = response.json()['user_id']
            session["device_id"] = response.json()['device_id']
            session["access_token"] = response.json()['access_token']
            return redirect('/')



@app.route("/logout")
def logout():
    response = requests.post(f'{session["homeserver"]}/_matrix/client/r0/logout?access_token={session["access_token"]}')
    
    if response.status_code != 200:
        return redirect('/', response='Logout error ocurred')
    
    session["logout_status"] = True

    session.clear()
    return redirect('/')