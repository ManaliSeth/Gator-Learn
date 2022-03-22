# Class: CSC-648-848 Fall 2021
# Author: Manali Seth, Aarshil Patel
# Description: Contains queries to insert details in database

from project import flask_app
from flaskext.mysql import MySQL

mysql = MySQL()
mysql.init_app(flask_app)


class UserDAO:

    # Inserting user registration details to database
    def insertRegData(self,userVO):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("Select max(loginId) as loginId from Login")
        recentLogin = cursor.fetchone()

        userVO.user_loginId = str(recentLogin[0])

        cursor.execute(
            "Insert into User(userName, user_loginId) values ('" + str(userVO.userName) + "', '" + str(
                userVO.user_loginId) + "')")

        insertUser = cursor.fetchall()

        conn.commit()
        cursor.close()
        conn.close()


