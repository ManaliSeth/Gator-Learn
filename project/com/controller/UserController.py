from project import flask_app
from flask import render_template,session, request, Response
from project.com.vo.UserVO import UserVO
from project.com.dao.UserDAO import UserDAO
from project.com.vo.LoginVO import LoginVO
from project.com.dao.LoginDAO import LoginDAO
from project.com.vo.MajorVO import MajorVO
from project.com.dao.MajorDAO import MajorDAO
from project.com.vo.CourseVO import CourseVO
from project.com.dao.CourseDAO import CourseDAO
from flaskext.mysql import MySQL
import json

@flask_app.route('/register',methods=['POST'])
def register():
    userVO = UserVO()
    userDAO = UserDAO()

    loginVO = LoginVO()
    loginDAO = LoginDAO()

    majorDAO = MajorDAO()
    majorDict = majorDAO.viewMajorName()

    courseDAO = CourseDAO()
    courseDict = courseDAO.viewCourseName()

    print("MajorDict=", majorDict)
    print("CourseDict=", courseDict)

    userName = request.form['userName']
    loginEmail = request.form['loginEmail']
    loginPassword = request.form['loginPassword']

    loginVO.loginEmail = loginEmail
    loginVO.loginPassword = loginPassword
    loginVO.loginStatus = "inactive"

    print(loginVO.loginEmail)
    print(loginVO.loginPassword)
    print(loginVO.loginStatus)
    loginDAO.insertLoginData(loginVO)

    userVO.userName = userName

    userDAO.insertRegData(userVO)

    return render_template('user/login.html', majorDict=majorDict, courseDict=courseDict)