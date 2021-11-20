from project import flask_app
# from flask import app
from flaskext.mysql import MySQL

# from project.com.dao import *

mysql = MySQL()
mysql.init_app(flask_app)
conn = mysql.connect()
cursor = conn.cursor()
cursor2 = conn.cursor()
cursor3 = conn.cursor()

class RegisteredUserDAO:

    def viewTutors(self):

        cursor.execute("Select * From RegisteredUser WHERE role='Tutor'")
        cursor2.execute("Select count(*) From RegisteredUser WHERE role='Tutor'")
        dict1 = cursor.fetchall()
        dict2 = cursor2.fetchall()
        return dict1, dict2

    def viewCourseTutors(self,registeredUserVO):

        cursor.execute("Select * From RegisteredUser WHERE role='Tutor' and courseTaught='"+str(registeredUserVO.search_input)+"' ")
        cursor2.execute("Select count(*) From RegisteredUser WHERE role='Tutor' and courseTaught='"+str(registeredUserVO.search_input)+"' ")
        cursor3.execute("Select count(*) From RegisteredUser WHERE role='Tutor'")
        dict1 = cursor.fetchall()
        dict2 = cursor2.fetchall()
        dict3 = cursor3.fetchall()
        return dict1, dict2, dict3