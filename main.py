# pip install gunicorn flask
# foreman start
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'
