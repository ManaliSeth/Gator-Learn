from project import flask_app
# from flask import app
from flaskext.mysql import MySQL

# from project.com.dao import *

mysql = MySQL()
mysql.init_app(flask_app)

class LoginDAO:

    def insertLoginData(self,loginVO):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "Insert into Login(loginEmail,loginPassword,loginStatus) values ('" + str(loginVO.loginEmail) + "', '" + str(loginVO.loginPassword) + "', '" + str(loginVO.loginStatus) + "')")
        dict1 = cursor.fetchall()
        print(dict1)
        conn.commit()
        cursor.close()
        conn.close()


    def checkLoginCredentials(self, loginVO):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Login WHERE loginEmail = '"+str(loginVO.loginEmail)+"' and loginPassword = '"+str(loginVO.loginPassword)+"'")
        dict1 = cursor.fetchall()
        print(dict1)
        conn.commit()
        cursor.close()
        conn.close()
        return dict1

    def updateLoginStatus(self,loginVO):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Login SET loginStatus = '"+ loginVO.loginStatus +"'  ")
        dict1 = cursor.fetchall()
        print(dict1)
        conn.commit()
        cursor.close()
        conn.close()
        return dict1