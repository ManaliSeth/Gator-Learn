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

@flask_app.route('/insertData',methods=['POST'])
def regData():

    unregisteredUserVO = UnregisteredUserVO()
    unregisteredUserDAO = UnregisteredUserDAO()

    name = request.form['name']
    #firstName = request.form['firstname']
    #lastName = request.form['lastname']
    #age = request.form['age']
    #gender = request.form['gender']
    email = request.form['email']
    password = request.form['password']
    confirmPassword = request.form['cpassword']
    #avatar = request.form['avatar']
    #description = request.form['description']
    #status = request.form['status']
    #role = request.form['role']
    #courseTaught = request.form['coursetaught']


    unregisteredUserVO.name = name
    unregisteredUserVO.email = email
    unregisteredUserVO.password = password

    unregisteredUserDAO.insertData(unregisteredUserVO)

    return render_template('user/login.html')
