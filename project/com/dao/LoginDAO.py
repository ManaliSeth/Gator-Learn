# Class: CSC-648-848 Fall 2021
# Author: Manali Seth, Aarshil Patel
# Description: Contains queries to insert details and fetch from database

from project import flask_app
from flaskext.mysql import MySQL

mysql = MySQL()
mysql.init_app(flask_app)

class LoginDAO:

    # Inserting login creds in database
    def insertLoginData(self,loginVO):

        conn = mysql.connect()
        cursor = conn.cursor()

        cursor.execute(
            #"Insert into Login(loginEmail,loginPassword,loginStatus) values ('" + str(loginVO.loginEmail) + "', '" + str(loginVO.loginPassword) + "', '" + str(loginVO.loginStatus) + "')")
            "Insert into Login(loginEmail,loginPassword,loginStatus) values ('" + str(
                loginVO.loginEmail) + "', '" + str(loginVO.hashedPassword) + "', '" + str(loginVO.loginStatus) + "')")

        insertLoginData = cursor.fetchall()
        print(insertLoginData)
        conn.commit()
        cursor.close()
        conn.close()

    # Checking if user is already registered
    def checkAlreadyRegistered(self, loginVO):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM Login WHERE loginEmail = '" + str(loginVO.loginEmail) + "' ")
        emailCheck = cursor.fetchall()
        print(emailCheck)
        conn.commit()
        cursor.close()
        conn.close()
        return emailCheck

    # Fetching password for email filled which is to be hashed
    def checkPassword(self, loginVO):

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Login WHERE loginEmail = '"+str(loginVO.loginEmail)+"'")
        dict1 = cursor.fetchall()

        conn.commit()
        cursor.close()
        conn.close()
        return dict1


    def updateLoginStatus(self,loginVO):
        pass
        #     conn = mysql.connect()
        #     cursor = conn.cursor()
        #     print(loginVO.loginId)
        #     cursor.execute("UPDATE Login SET loginStatus = '"+ str(loginVO.loginStatus) +"' where loginId = '"+str(loginVO.loginId)+"' ")
        #     dict1 = cursor.fetchall()
        #     print(dict1)
        #     conn.commit()
        #     cursor.close()
        #     conn.close()
        #     return dict1
    # Comparing login creds entered in form with creds stored in database
    def checkLoginCredentials(self, loginVO):

        conn = mysql.connect()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM Login WHERE loginEmail = '" + str(loginVO.loginEmail) + "' and loginPassword = '" + str(
                loginVO.loginPassword) + "'")

        checkLoginCred = cursor.fetchall()

        conn.commit()
        cursor.close()
        conn.close()
        return checkLoginCred

