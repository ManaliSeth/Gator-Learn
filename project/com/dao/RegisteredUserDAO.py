from project import flask_app
# from flask import app
from flaskext.mysql import MySQL

# from project.com.dao import *

mysql = MySQL()
mysql.init_app(flask_app)
conn = mysql.connect()
cursor = conn.cursor()

class RegisteredUserDAO:

    def viewTutors(self):

        cursor.execute("Select * From RegisteredUser WHERE role='Tutor'")
        dict1 = cursor.fetchall()
        return dict1

    def viewCourseTutors(self,registeredUserVO):

        cursor.execute("Select * From RegisteredUser WHERE role='Tutor' and courseTaught='"+str(registeredUserVO.search_input)+"' ")
        dict1 = cursor.fetchall()
        return dict1