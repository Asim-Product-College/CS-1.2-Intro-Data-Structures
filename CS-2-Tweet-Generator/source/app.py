# An instance of this class will be our WSGI application.
from flask import Flask
from randomsentence import *
# from randomsentence import

# Next we create an instance of this class
# first arg is name of the application’s module or package. 
app = Flask(__name__)
# decorator to tell Flask what URL should trigger our function.
@app.route('/')
def index():
    return main()