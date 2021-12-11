from project import flask_app
from flask import render_template,session, request, Response
from project.com.dao.MajorDAO import MajorDAO
from project.com.dao.CourseDAO import CourseDAO
from project.com.vo.RegisteredUserVO import RegisteredUserVO
from project.com.dao.RegisteredUserDAO import RegisteredUserDAO
from project.com.vo.UnregisteredUserVO import UnregisteredUserVO
from project.com.dao.UnregisteredUserDAO import UnregisteredUserDAO
from flaskext.mysql import MySQL
import json

@flask_app.route('/searchData',methods=['POST'])
def loginData():
    registeredUserVO = RegisteredUserVO()
    registeredUserDAO = RegisteredUserDAO()

    email = request.form['email']
    password = request.form['password']

    registeredUserVO.email = email
    registeredUserVO.password = password

    credentials = registeredUserDAO.searchData(registeredUserVO)
    print(credentials)
    if len(credentials) == 0:
        return render_template("user/login.html", errorMsg="Username or password is incorrect")


    return render_template("user/loginLandingPage.html")