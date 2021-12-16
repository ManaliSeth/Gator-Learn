from project import flask_app
from flask import render_template, session
from project.com.dao.MajorDAO import MajorDAO
from project.com.dao.CourseDAO import CourseDAO
from project.com.dao.CatalogDAO import CatalogDAO
from flaskext.mysql import MySQL

mysql = MySQL()
mysql.init_app(flask_app)
conn = mysql.connect()
cursor = conn.cursor()

@flask_app.route('/catalog',methods=['GET'])
def catalog():

    majorDAO = MajorDAO()
    majorDict = majorDAO.viewMajorName()
    courseDAO = CourseDAO()
    courseDict = courseDAO.viewCourseName()
    catalogDAO = CatalogDAO()
    catalogTuple, catalogTotalCountTuple = catalogDAO.viewCatalog()
    print("Catalog Tuple = ",catalogTuple)
    catalogDict = {}
    for i in catalogTuple:
        if i[0] in catalogDict.keys():
            catalogDict[i[0]].append(i[1])
        else:
            catalogDict[i[0]] = [i[1]]

    list1 = []
    for i in catalogTotalCountTuple:
        list1.append(i[0])
    print("list1=",list1)
    catalogTotalCountTuple = list1

    if 'loginId' in session:
        return render_template('user/loginCatalog.html', courseDict=courseDict, catalogDict=catalogDict, catalogTotalCountTuple=catalogTotalCountTuple, majorDict=majorDict)
    else:
        return render_template('user/catalog.html', courseDict=courseDict, catalogDict=catalogDict,
                               catalogTotalCountTuple=catalogTotalCountTuple, majorDict=majorDict)