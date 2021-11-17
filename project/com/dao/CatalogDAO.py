from project import flask_app
# from flask import app
from flaskext.mysql import MySQL

# from project.com.dao import *

mysql = MySQL()
mysql.init_app(flask_app)
conn = mysql.connect()
cursor = conn.cursor()

class CatalogDAO:

    def viewCatalog(self):

        cursor.execute("select majorName,courseName from Major M, Catalog C, Courses Co where M.majorId=C.majorId and Co.courseNo=C.courseNo;")
        dict1 = cursor.fetchall()
        print(dict1)
        return dict1