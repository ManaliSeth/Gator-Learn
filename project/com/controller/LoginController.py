
# Class: CSC-648-848 Fall 2021
# Author: Manali Seth, Seela Pant
# Description: Contains flask routes to navigate between frontend and backend. Contains logic

from project import flask_app
from flask import render_template, session, request, redirect, url_for, flash
from project.com.vo.LoginVO import LoginVO
from project.com.dao.LoginDAO import LoginDAO
from project.com.dao.MajorDAO import MajorDAO
from project.com.dao.CourseDAO import CourseDAO
from passlib.hash import pbkdf2_sha256

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

    # Fetching password for email filled which is to be hashed
    loginCred = loginDAO.checkPassword(loginVO)

    if len(loginCred)==0:
        flash("Not registered email. Register Now!")
        return redirect(url_for('userLoadRegister'))

    else:
        hashedPassword = loginCred[0][2]
        print("Hashed pwd=", hashedPassword)

        password_verify = pbkdf2_sha256.verify(str(loginVO.loginPassword),hashedPassword)
        print("Password Verify=",password_verify)

        if password_verify:
            session['loginId'] = loginCred[0][0]
            loginVO.loginId = session['loginId']
            return redirect(url_for('loginLandingPage'))

        else:
            flash("Username or password is incorrect")
            return redirect(url_for('userLoadLogin'))


@flask_app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('landingPage'))
