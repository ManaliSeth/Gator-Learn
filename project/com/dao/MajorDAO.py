from project import flask_app
# from flask import app
from flaskext.mysql import MySQL

# from project.com.dao import *

mysql = MySQL()
mysql.init_app(flask_app)
conn = mysql.connect()
cursor = conn.cursor()

class MajorDAO:

    def viewMajorName(self):

        cursor.execute("select * from Major")
        dict1 = cursor.fetchall()
        print(dict1)
        return dict1