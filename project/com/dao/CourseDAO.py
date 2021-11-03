from project import flask_app
# from flask import app
from flaskext.mysql import MySQL

# from project.com.dao import *

mysql = MySQL()
mysql.init_app(flask_app)
conn = mysql.connect()
cursor = conn.cursor()

class CourseDAO:

    def viewCourseName(self):

        cursor.execute("Select courseName From Courses")
        dict1 = cursor.fetchall()
        return dict1