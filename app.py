from flask import Flask, render_template, request, redirect
from include import userLogin

app = Flask(__name__)

app.config["TEMPLATE_AUTO_RELOAD"] = True

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

        response = userLogin.clientLogin(username, password, f'https://{homeserver}')
        
        if hasattr(response, 'message'):
            print(f'{response.message}')

            return render_template("login.html", response=response.message)
        else:
            return redirect('/')