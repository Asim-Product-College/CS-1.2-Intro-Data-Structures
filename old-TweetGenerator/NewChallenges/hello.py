from flask import Flask
from random_sentence import *
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
