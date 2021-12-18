
# Class: CSC-648-848 Fall 2021
# Author: Manali Seth, Aarshil Patel
# Description: Contains flask routes to navigate between frontend and backend. Contains logic.

from project import flask_app
from flask import render_template,session, request, redirect, url_for
from project.com.dao.MajorDAO import MajorDAO
from project.com.dao.CourseDAO import CourseDAO
from project.com.dao.TutorPostingDAO import TutorPostingDAO
from project.com.vo.MessageVO import MessageVO
from project.com.dao.MessageDAO import MessageDAO
import datetime

@flask_app.route('/sendMessage',methods=['POST'])
def sendMessage():

    if 'loginId' in session:

        messageVO = MessageVO()
        messageDAO = MessageDAO()

        currentDT = datetime.datetime.now()

        msgTo_loginId = request.form['msgTo_loginId']
        msgFrom_loginId = session['loginId']
        msg_forCourse = request.form['msg_forCourse']
        msg_forMajor = request.form['msg_forMajor']
        msgDesc = request.form['msgDesc']
        msgDate = currentDT.strftime("%Y/%m/%d")
        msgTime = currentDT.strftime("%H:%M:%S")

        messageVO.msg_forMajor = msg_forMajor
        messageVO.msg_forCourse = msg_forCourse

        # Fetching majorId based on major name
        msg_majorId = messageDAO.viewMsgMajorId(messageVO)

        # Fetching course no. based on course name
        msg_courseNo = messageDAO.viewMsgCourseNo(messageVO)

        messageVO.msgTo_loginId = msgTo_loginId
        messageVO.msgFrom_loginId = msgFrom_loginId
        messageVO.msg_majorId = msg_majorId[0][0]
        messageVO.msg_courseNo = msg_courseNo[0][0]
        messageVO.msgDesc = msgDesc
        messageVO.msgDate = msgDate
        messageVO.msgTime = msgTime

        # Inserting message contents in database
        messageDAO.insertMessage(messageVO)

        return redirect(url_for('loginLandingPage'))

    else:

        return redirect(url_for('userLoadRegister'))


@flask_app.route('/readMessage')
def readMessage():

    if 'loginId' in session:
        loginId = session['loginId']

        majorDAO = MajorDAO()

        # Listing all majors for search bar (All Major dropdown)
        majorDict = majorDAO.viewMajorName()

        courseDAO = CourseDAO()

        # Fetching all courses names for search bar
        courseDict = courseDAO.viewCourseName()

        tutorPostingDAO = TutorPostingDAO()

        # Fetching recent 3 approved tutor postings
        tutorDict = tutorPostingDAO.viewRecentTutorPostings()

        messageVO = MessageVO()
        messageDAO = MessageDAO()

        messageVO.msgTo_LoginId = loginId

        # Fetching message contents from database
        messageDict, messageCountDict = messageDAO.readMessage(messageVO)

        return render_template('user/loginLandingPage.html', messageDict=messageDict, messageCountDict=messageCountDict,
                               isOffcanvas='is-offcanvas', majorDict=majorDict, courseDict=courseDict,
                               tutorDict=tutorDict)

    else:
        return redirect(url_for('userLoadLogin'))

@flask_app.route('/insertMessage', methods=['POST'])
def insertMessage():

    if 'loginId' in session:

        messageVO = MessageVO()
        messageDAO = MessageDAO()

        currentDT = datetime.datetime.now()

        msgTo_loginId = request.form['msgTo_loginId']
        msgFrom_loginId = session['loginId']
        msg_forCourse = request.form['msg_forCourse']
        msg_forMajor = request.form['msg_forMajor']
        msgDesc = request.form['msgDesc']
        msgDate = currentDT.strftime("%Y/%m/%d")
        msgTime = currentDT.strftime("%H:%M:%S")

        messageVO.msg_forMajor = msg_forMajor
        messageVO.msg_forCourse = msg_forCourse

        # Fetching majorId based on major name
        msg_majorId = messageDAO.viewMsgMajorId(messageVO)

        # Fetching course no. based on course name
        msg_courseNo = messageDAO.viewMsgCourseNo(messageVO)

        messageVO.msgTo_loginId = msgTo_loginId
        messageVO.msgFrom_loginId = msgFrom_loginId
        messageVO.msg_majorId = msg_majorId[0][0]
        messageVO.msg_courseNo = msg_courseNo[0][0]
        messageVO.msgDesc = msgDesc
        messageVO.msgDate = msgDate
        messageVO.msgTime = msgTime

        # Inserting message contents in database
        messageDAO.insertMessage(messageVO)

        return redirect(url_for('loginLandingPage'))

    else:

        return redirect(url_for('userLoadRegister'))


