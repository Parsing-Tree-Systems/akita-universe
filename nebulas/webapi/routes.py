import os
import secrets
from flask import request

from . import app

from webapi.repository import *
# from webapi.models import *

@app.get('/')
def index():
    return 'Index Page'

@app.post('/login/')
def login():
    email = request.form['email']
    password = request.form['password']
    if is_valid(request):
        # session['email'] = email
        return 'Login Successful'
    else:
        error = 'Invalid UserId / Password'
        return error

@app.post("/register/")
def register():
    msg = extractAndPersistUserDataFromForm(request)
    return msg

@app.get("/heartbeat/")
def heart_beat():
    return 'appication is up and running'
        