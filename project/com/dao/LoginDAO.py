from project import flask_app
# from flask import app
from flaskext.mysql import MySQL
from passlib.hash import pbkdf2_sha256

# from project.com.dao import *

mysql = MySQL()
mysql.init_app(flask_app)

class LoginDAO:

    def insertLoginData(self,loginVO):

        password = pbkdf2_sha256.hash(str(loginVO.loginPassword))

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            #"Insert into Login(loginEmail,loginPassword,loginStatus) values ('" + str(loginVO.loginEmail) + "', '" + str(loginVO.loginPassword) + "', '" + str(loginVO.loginStatus) + "')")
            "Insert into Login(loginEmail,loginPassword,loginStatus) values ('" + str(
                loginVO.loginEmail) + "', '" + password + "', '" + str(loginVO.loginStatus) + "')")

        dict1 = cursor.fetchall()
        print(dict1)
        conn.commit()
        cursor.close()
        conn.close()


    def checkLoginCredentials(self, loginVO):

        #password_verify = pbkdf2_sha256.verify(str(loginVO.loginPassword), loginPassword)

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Login WHERE loginEmail = '"+str(loginVO.loginEmail)+"' and loginPassword = '"+str(loginVO.loginPassword)+"'")
        dict1 = cursor.fetchall()
        print(dict1)
        conn.commit()
        cursor.close()
        conn.close()
        return dict1

    def checkPassword(self, loginVO):


        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT loginPassword FROM Login WHERE loginEmail = '"+str(loginVO.loginEmail)+"'")
        dict1 = cursor.fetchall()
        print(dict1[0][0])
        print(str(loginVO.loginPassword))

        password_verify = pbkdf2_sha256.verify(str(loginVO.loginPassword), dict1[0][0])
        print(password_verify)
        conn.commit()
        cursor.close()
        conn.close()
        return dict1[0][0]

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