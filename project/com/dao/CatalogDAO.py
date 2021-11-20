from project import flask_app
# from flask import app
from flaskext.mysql import MySQL

# from project.com.dao import *

mysql = MySQL()
mysql.init_app(flask_app)
conn = mysql.connect()
cursor = conn.cursor()
cursor2 = conn.cursor()
# cursor3 = conn.cursor()

class CatalogDAO:

    def viewCatalog(self):

        cursor.execute("select majorName,courseName from Major M, Catalog C, Courses Co where M.majorId=C.majorId and Co.courseNo=C.courseNo;")
        # cursor2.execute(
        #     "select count(majorName) from Major M, Catalog C, Courses Co where M.majorId=C.majorId and Co.courseNo=C.courseNo;")
        cursor2.execute(
            "select count(distinct(majorId)) from Catalog;")
        dict1 = cursor.fetchall()
        dict2 = cursor2.fetchall()
        # dict3 = cursor3.fetchall()
        print(dict1)
        return dict1, dict2