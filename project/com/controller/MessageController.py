from project import flask_app
from flask import render_template,session, request, Response, redirect, url_for
from project.com.dao.MajorDAO import MajorDAO
from project.com.dao.CourseDAO import CourseDAO
from project.com.vo.RegisteredUserVO import RegisteredUserVO
from project.com.dao.RegisteredUserDAO import RegisteredUserDAO
from project.com.vo.UnregisteredUserVO import UnregisteredUserVO
from project.com.dao.UnregisteredUserDAO import UnregisteredUserDAO
from project.com.vo.MessageVO import MessageVO
from project.com.dao.MessageDAO import MessageDAO
from flaskext.mysql import MySQL
import json
import datetime

@flask_app.route('/sendMessage',methods=['POST'])
def sendMessage():

    if 'loginId' in session:
        print("Session loginId = ",session['loginId'])
        messageVO = MessageVO()
        messageDAO = MessageDAO()

        currentDT = datetime.datetime.now()

        msgTo_userId = request.form['tutorId']
        msgFrom_userId = session['loginId']
        msgDesc = request.form['msgDesc']
        msgDate = currentDT.strftime("%Y/%m/%d")
        msgTime = currentDT.strftime("%H:%M:%S")

        messageVO.msgTo_userId = msgTo_userId
        messageVO.msgFrom_userId = msgFrom_userId
        messageVO.msgDesc = msgDesc
        messageVO.msgDate = msgDate
        messageVO.msgTime = msgTime

        messageDAO.insertMessage(messageVO)

        return redirect(url_for('loginLandingPage'))

    else:
        return redirect(url_for('userLoadRegister'))