# Class: CSC-648-848 Fall 2021
# Author: Manali Seth
# Description: Contains queries to fetch catalog details from database

from project import flask_app
from flaskext.mysql import MySQL

mysql = MySQL()
mysql.init_app(flask_app)
conn = mysql.connect()
cursor = conn.cursor()
cursor2 = conn.cursor()

class CatalogDAO:

    # Fetching all majors and courses for full SFSU catalog
    def viewCatalog(self):
        cursor.execute(
            "select majorName,courseName from Major M, Catalog C, Courses Co where M.majorId=C.majorId and Co.courseNo=C.courseNo;")
        cursor2.execute(
            "select count(distinct(majorId)) from Catalog;")
        catalog = cursor.fetchall()
        catalogCount = cursor2.fetchall()
        return catalog, catalogCount