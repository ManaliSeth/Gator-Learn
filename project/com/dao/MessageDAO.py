from project import flask_app
# from flask import app
from flaskext.mysql import MySQL

# from project.com.dao import *

mysql = MySQL()
mysql.init_app(flask_app)

class MessageDAO():

    def insertMessage(self,messageVO):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("Insert into Messaging (msgTo_loginId, msgFrom_loginId, msg_majorId, msg_courseNo, msgDate, msgTime, msgDesc) values('"+ str(messageVO.msgTo_loginId) +"', '"+ str(messageVO.msgFrom_loginId) +"', '"+ str(messageVO.msg_majorId) +"', '"+ str(messageVO.msg_courseNo) +"', '"+ str(messageVO.msgDate) +"', '"+ str(messageVO.msgTime) +"', '"+ messageVO.msgDesc +"')")
        dict1 = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return dict1

    def viewMsgMajorId(self, messageVO):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("Select majorId from Major where majorName='"+str(messageVO.msg_forMajor)+"'")
        msgMajorDict = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return msgMajorDict

    def viewMsgCourseNo(self, messageVO):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("Select courseNo from Courses where courseName='"+str(messageVO.msg_forCourse)+"'")
        msgCourseDict = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return msgCourseDict

    def readMessage(self, messageVO):

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor2 = conn.cursor()
        cursor.execute("Select M.*,U.userName, Ma.majorName, Co.courseName from Messaging M, User U, Major Ma, Courses Co where U.user_loginId = M.msgFrom_LoginId and M.msg_majorId=Ma.majorId and M.msg_courseNo=Co.courseNo and M.msgTo_LoginId = '"+str(messageVO.msgTo_LoginId)+"' ")
        cursor2.execute("Select count(*) From (Select M.*,U.userName, Ma.majorName, Co.courseName from Messaging M, User U, Major Ma, Courses Co where U.user_loginId = M.msgFrom_LoginId and M.msg_majorId=Ma.majorId and M.msg_courseNo=Co.courseNo and M.msgTo_LoginId = '"+str(messageVO.msgTo_LoginId)+"') x ")

        messageDict = cursor.fetchall()
        messageCountDict = cursor2.fetchall()

        conn.commit()
        cursor.close()
        cursor2.close()
        conn.close()
        return messageDict, messageCountDict

