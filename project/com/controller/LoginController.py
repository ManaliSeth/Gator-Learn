
# Class: CSC-648-848 Fall 2021
# Author: Mnaali Seth, Seela Pant
# Description: Contains flask routes to navigate between frontend and backend. Contains logic

from project import flask_app
from flask import render_template, session, request, redirect, url_for
from project.com.vo.LoginVO import LoginVO
from project.com.dao.LoginDAO import LoginDAO
from project.com.dao.MajorDAO import MajorDAO
from project.com.dao.CourseDAO import CourseDAO

@flask_app.route('/login', methods=['POST'])
def login():

    loginVO = LoginVO()
    loginDAO = LoginDAO()

    majorDAO = MajorDAO()

    # Listing all majors for search bar (All Major dropdown)
    majorDict = majorDAO.viewMajorName()

    courseDAO = CourseDAO()

    # Fetching all courses names for search bar
    courseDict = courseDAO.viewCourseName()

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

    # Comparing login creds entered in form with creds stored in database
    # loginCredDict = loginDAO.checkLoginCredentials(loginVO)

    # loginCred =[]
    # for i in loginCredDict:
    #     loginCred.append(i)
    #
    # loginCredDict = loginCred

    # if len(loginCredDict) == 0:
    #     return render_template("user/login.html", errorMsg="Username or password is incorrect", majorDict=majorDict,
    #                            courseDict=courseDict)
    #
    # elif loginVO.loginPassword != loginCredDict[0][2]:
    #     return render_template('user/login.html', errorMsg=' Username or Password is incorrect !', majorDict=majorDict,
    #                            courseDict=courseDict)
    #
    # else:
    #
    #     loginVO.loginStatus = "active"
    #     session['loginId'] = loginCredDict[0][0]
    #     loginVO.loginId = session['loginId']
    #     loginDAO.updateLoginStatus(loginVO)


@flask_app.route('/logout')
def logout():
    # loginVO = LoginVO()
    # loginDAO = LoginDAO()
    # loginDAO.loginStatus = "inactive"
    # loginVO.loginId = session['loginId']
    # print(type(loginVO.loginId))
    # loginDAO.updateLoginStatus(loginVO)
    session.clear()
    # session['loginId'] = None
    return redirect(url_for('landingPage'))
