from flask import Flask, render_template, request
import datetime


app = Flask(__name__)

date = datetime.datetime.now()

@app.route("/")
def hello_world():
    return render_template("index.html", x=date)
