from project import flask_app
from flask import render_template,session, request, Response, redirect, url_for
from project.com.vo.LoginVO import LoginVO
from project.com.dao.LoginDAO import LoginDAO
from project.com.vo.MajorVO import MajorVO
from project.com.dao.MajorDAO import MajorDAO
from project.com.vo.CourseVO import CourseVO
from project.com.dao.CourseDAO import CourseDAO
from flaskext.mysql import MySQL
import json

@flask_app.route('/login', methods=['POST'])
def login():

    loginVO = LoginVO()
    loginDAO = LoginDAO()

    majorDAO = MajorDAO()
    majorDict = majorDAO.viewMajorName()

    courseDAO = CourseDAO()
    courseDict = courseDAO.viewCourseName()

    print("MajorDict=", majorDict)
    print("CourseDict=", courseDict)

    loginEmail = request.form['loginEmail']
    loginPassword = request.form['loginPassword']

    loginVO.loginEmail = loginEmail
    loginVO.loginPassword = loginPassword

    # loginCredDict = loginDAO.checkLoginCredentials(loginVO)
    # print(loginCredDict)

    loginCredDict2 = loginDAO.checkPassword(loginVO)
    print(loginCredDict2)

    # list1 =[]
    # for i in loginCredDict2:
    #     list1.append(i)
    # print("list1=", list1)
    # loginCredDict2 = list1
    # print(loginCredDict2)

    # if len(loginCredDict2) == 0:
    #     return render_template("user/login.html", errorMsg="Username or password is incorrect")
    #
    #
    # elif loginVO.loginPassword != loginCredDict2:
    #     return render_template('user/login.html', errorMsg2='Password is Incorrect !')
    #
    # else:
    #     loginVO.loginStatus = "active"
    #     loginDAO.updateLoginStatus(loginVO)
    #     session['loginId'] = loginCredDict2
    #     return redirect(url_for('loginLandingPage'))

    if loginCredDict2:
        loginVO.loginStatus = "active"
        loginDAO.updateLoginStatus(loginVO)
        session['loginId'] = loginCredDict2
        return redirect(url_for('loginLandingPage'))

    else:
        return render_template("user/login.html", errorMsg="Username or password is incorrect")


@flask_app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('landingPage'))
