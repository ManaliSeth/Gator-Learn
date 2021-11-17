from project import flask_app
from flask import render_template
from project.com.dao.MajorDAO import MajorDAO
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
    catalogDAO = CatalogDAO()
    catalogTuple = catalogDAO.viewCatalog()
    print("Catalog Tuple = ",catalogTuple)
    catalogDict = {}
    for i in catalogTuple:
        if i[0] in catalogDict.keys():
            catalogDict[i[0]].append(i[1])
        else:
            catalogDict[i[0]] = [i[1]]
    return render_template('user/catalog.html',catalogDict=catalogDict,majorDict=majorDict)