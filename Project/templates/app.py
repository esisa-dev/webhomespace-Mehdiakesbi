from flask import(
    Flask,
    request,
    render_template,
    redirect,
    session,
    url_for,

)
from dal import userdao
import os

app = Flask(__name__,template_folder="template",static_folder = 'static')

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/logout')
def logout():
    return render_template("index2.html")

@app.route("/login",methods =["GET","POST"])
def home():
    global fixUsername
    global pathcurent
    usr : str = request.form['username']
    pwd : str = request.form['password']
    login =userdao(username,password)
    if username != "" :
        if login.Check() == True:   
            Username = username
            chemin = "/home/"+username
            return render_template("index.html",directory = gsFiledr.getPath("/home/"+username) )
    return render_template("index.html",erreur = "username or password incorrect ")
