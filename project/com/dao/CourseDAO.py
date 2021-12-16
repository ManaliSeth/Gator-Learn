# Class: CSC-648-848 Fall 2021
# Author: Manali Seth
# Description: Contains queries to fetch details from database

from project import flask_app
from flaskext.mysql import MySQL

mysql = MySQL()
mysql.init_app(flask_app)
conn = mysql.connect()
cursor = conn.cursor()

class CourseDAO:

    # Fetching all courses names for search bar
    def viewCourseName(self):

        cursor.execute("Select courseName From Courses")
        courseName = cursor.fetchall()
        return courseName

    # Fetching course name based on Major
    def viewCourseMajors(self,majorVO):

        cursor.execute(
            "Select majorName,courseName From Major M, Catalog C, Courses Co where M.majorId=C.majorId and Co.courseNo=C.courseNo")
        courseMajor = cursor.fetchall()
        return courseMajor