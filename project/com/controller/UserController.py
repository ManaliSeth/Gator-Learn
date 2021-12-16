# Class: CSC-648-848 Fall 2021
# Author: Manali Seth, Christian Robert Samatra
# Description: Contains flask routes to navigate between frontend and backend. Contains logic

from project import flask_app
from flask import render_template, request
from project.com.vo.UserVO import UserVO
from project.com.dao.UserDAO import UserDAO
from project.com.vo.LoginVO import LoginVO
from project.com.dao.LoginDAO import LoginDAO
from project.com.dao.MajorDAO import MajorDAO
from project.com.dao.CourseDAO import CourseDAO

@flask_app.route('/register',methods=['POST'])
def register():

    userVO = UserVO()
    userDAO = UserDAO()

    loginVO = LoginVO()
    loginDAO = LoginDAO()

    majorDAO = MajorDAO()

    # Listing all majors for search bar (All Major dropdown)
    majorDict = majorDAO.viewMajorName()

    courseDAO = CourseDAO()

    # Fetching all courses names for search bar
    courseDict = courseDAO.viewCourseName()

    userName = request.form['userName']
    loginEmail = request.form['loginEmail']
    loginPassword = request.form['loginPassword']

    loginVO.loginEmail = loginEmail
    loginVO.loginPassword = loginPassword
    loginVO.loginStatus = "inactive"

    # Inserting login creds in database
    loginDAO.insertLoginData(loginVO)

    userVO.userName = userName

    # Inserting user registration details to database
    userDAO.insertRegData(userVO)

    return render_template('user/login.html', majorDict=majorDict, courseDict=courseDict)




