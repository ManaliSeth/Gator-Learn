from project import flask_app
from flask import render_template,session, request, Response, redirect, url_for
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
        msgDesc = request.form['msgDesc']
        msgDate = currentDT.strftime("%Y/%m/%d")
        msgTime = currentDT.strftime("%H:%M:%S")

        messageVO.msgTo_loginId = msgTo_loginId
        messageVO.msgFrom_loginId = msgFrom_loginId
        messageVO.msgDesc = msgDesc
        messageVO.msgDate = msgDate
        messageVO.msgTime = msgTime

        messageDAO.insertMessage(messageVO)

        return redirect(url_for('loginLandingPage'))

    else:
        return redirect(url_for('userLoadRegister'))