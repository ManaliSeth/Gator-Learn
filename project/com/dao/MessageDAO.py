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
        cursor.execute("Insert into Messaging (msgTo_userId, msgFrom_userId, msgDate, msgTime, msgDesc) values('"+ str(messageVO.msgTo_userId) +"', '"+ str(messageVO.msgFrom_userId) +"','"+ str(messageVO.msgDate) +"', '"+ str(messageVO.msgTime) +"', '"+ messageVO.msgDesc +"')")
        dict1 = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return dict1