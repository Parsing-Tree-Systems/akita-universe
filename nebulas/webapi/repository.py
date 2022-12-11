import hashlib
from MySQLdb import Date
from flask import url_for, flash, redirect, session

from . import mysql
# from webapi.models import *

def is_valid(request):
    # Using Flask-SQLAlchmy ORM
    # data = User.query.with_entities(User.email, User.password).all()

    # Using Raw SQL Select Query
    email = request.form['email']
    password = request.form['password']
    cur = mysql.connection.cursor()
    
    cur.execute("SELECT email, password FROM users")
    userData = cur.fetchall()
    cur.close()

    for row in userData:
        if row['email'] == email and row['password'] == hashlib.md5(password.encode()).hexdigest():
            return True
    return False

def extractAndPersistUserDataFromForm(request):
    password = request.form['password']
    email = request.form['email']
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    phone = request.form['phone']
    createdOn = request.form['createdOn']

    cur = mysql.connection.cursor()

    # user = User(fname=firstName, lname=lastName, 
    #     password=hashlib.md5(password.encode()).hexdigest(),
    #             email=email, phone=phone)
    
    values = (firstName,lastName,email,hashlib.md5(password.encode()).hexdigest(),phone,createdOn)
    
    try:
        cur.execute(
            ''' INSERT INTO users VALUES(%s,%s,%s,%s,%s,%s)''',
            values
        )
        mysql.connection.commit()
    except (
        mysql.connection.Error,
        mysql.connection.Warning
    ) as e:
        # print(format(e))
        return e.IntegrityError

    cur.close()

    return "Registered Successfully"