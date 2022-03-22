# Class: CSC-648-848 Fall 2021
# Author: Manali Seth
# Description: Contains queries to fetch details from database

from project import flask_app
from flaskext.mysql import MySQL

mysql = MySQL()
mysql.init_app(flask_app)
conn = mysql.connect()
cursor = conn.cursor()

class MajorDAO:

    # Listing all majors for search bar (All Major dropdown)
    def viewMajorName(self):

        cursor.execute("select * from Major")
        dict1 = cursor.fetchall()
        print(dict1)
        return dict1