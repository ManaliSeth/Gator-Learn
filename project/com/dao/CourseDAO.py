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

    def viewCourseMajors(self,majorVO):

        # cursor.execute("Select majorName,courseName From Major M, Catalog C, Courses Co where M.majorId=C.majorId and Co.courseNo=C.courseNo and M.majorId in (Select majorId from Major M where majorId='"+str(majorVO.majorId)+"' ) ")
        cursor.execute(
            "Select majorName,courseName From Major M, Catalog C, Courses Co where M.majorId=C.majorId and Co.courseNo=C.courseNo")
        dict1 = cursor.fetchall()
        return dict1