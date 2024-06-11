from flask import Flask
app=Flask(__name__)


@app.route("/")
def welcome():
    return("hi hello")

@app.route("/home")
def home():
    return("this is shannu")

from controller import *