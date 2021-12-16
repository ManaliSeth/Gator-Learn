from project import flask_app
from flask import render_template,session, request, Response, redirect, url_for
from project.com.dao.MajorDAO import MajorDAO
from project.com.dao.CourseDAO import CourseDAO
from project.com.dao.TutorPostingDAO import TutorPostingDAO
from project.com.vo.MessageVO import MessageVO
from project.com.dao.MessageDAO import MessageDAO
import datetime

@flask_app.route('/sendMessage',methods=['POST'])
def sendMessage():

    if 'loginId' in session:
        print("Session loginId = ",session['loginId'])
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

        msg_majorId = messageDAO.viewMsgMajorId(messageVO)
        print(msg_majorId)
        msg_courseNo = messageDAO.viewMsgCourseNo(messageVO)
        print(msg_courseNo)

        messageVO.msgTo_loginId = msgTo_loginId
        messageVO.msgFrom_loginId = msgFrom_loginId
        messageVO.msg_majorId = msg_majorId[0][0]
        messageVO.msg_courseNo = msg_courseNo[0][0]
        messageVO.msgDesc = msgDesc
        messageVO.msgDate = msgDate
        messageVO.msgTime = msgTime

        messageDAO.insertMessage(messageVO)

        return redirect(url_for('loginLandingPage'))

    else:
        return redirect(url_for('userLoadRegister'))


@flask_app.route('/readMessage')
def readMessage():

    loginId = session['loginId']
    print(loginId)

    majorDAO = MajorDAO()
    majorDict = majorDAO.viewMajorName()
    courseDAO = CourseDAO()
    courseDict = courseDAO.viewCourseName()
    print("MajorDict=", majorDict)
    print("CourseDict=", courseDict)
    tutorPostingDAO = TutorPostingDAO()
    tutorDict = tutorPostingDAO.viewRecentTutorPostings()
    print("Tutor Dict=", tutorDict)

    messageVO = MessageVO()
    messageDAO = MessageDAO()

    messageVO.msgTo_LoginId = loginId

    messageDict, messageCountDict = messageDAO.readMessage(messageVO)
    print("messageDict=",messageDict)
    print("messageCountDict=",messageCountDict)

    return render_template('user/loginLandingPage.html', messageDict=messageDict, messageCountDict=messageCountDict, isOffcanvas='is-offcanvas', majorDict=majorDict, courseDict=courseDict, tutorDict=tutorDict)





