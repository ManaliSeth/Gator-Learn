
# Class: CSC-648-848 Fall 2021
# Author: Manali Seth
# Description: Navigate between frontend (catalog.html) and backend. Contains flask routes to connect catalog page. Contains logics.

from project import flask_app
from flask import render_template, session
from project.com.dao.MajorDAO import MajorDAO
from project.com.dao.CourseDAO import CourseDAO
from project.com.dao.CatalogDAO import CatalogDAO
from flaskext.mysql import MySQL

mysql = MySQL()
mysql.init_app(flask_app)

@flask_app.route('/catalog',methods=['GET'])
def catalog():

    majorDAO = MajorDAO()

    # Listing all majors for search bar (All Major dropdown)
    majorDict = majorDAO.viewMajorName()

    courseDAO = CourseDAO()

    # Fetching all courses names for search bar
    courseDict = courseDAO.viewCourseName()

    catalogDAO = CatalogDAO()

    # Fetching all majors and courses for full SFSU catalog
    catalogTuple, catalogTotalCountTuple = catalogDAO.viewCatalog()

    catalogDict = {}
    for i in catalogTuple:
        if i[0] in catalogDict.keys():
            catalogDict[i[0]].append(i[1])
        else:
            catalogDict[i[0]] = [i[1]]

    catalogCountTuple = []
    for i in catalogTotalCountTuple:
        catalogCountTuple.append(i[0])
    catalogTotalCountTuple = catalogCountTuple

    if 'loginId' in session:
        return render_template('user/loginCatalog.html', courseDict=courseDict, catalogDict=catalogDict,
                               catalogTotalCountTuple=catalogTotalCountTuple, majorDict=majorDict)
    else:
        return render_template('user/catalog.html', courseDict=courseDict, catalogDict=catalogDict,
                               catalogTotalCountTuple=catalogTotalCountTuple, majorDict=majorDict)