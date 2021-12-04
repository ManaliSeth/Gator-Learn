from project import flask_app
# from flask import app
from flaskext.mysql import MySQL

# from project.com.dao import *

mysql = MySQL()
mysql.init_app(flask_app)
conn = mysql.connect()
cursor = conn.cursor()

class UnregisteredUserDAO:

    def insertData(self,unregisteredUserVO):
        cursor2 = conn.cursor()
        cursor2.execute("Insert into UnregisteredUser(name, email, password) values ('"+str(unregisteredUserVO.name)+"', '"+str(unregisteredUserVO.email)+"', '"+str(unregisteredUserVO.password)+"')")
        dict1 = cursor2.fetchall()
        conn.commit()
        cursor2.close()
        conn.close()
