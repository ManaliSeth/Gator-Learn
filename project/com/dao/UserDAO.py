from project import flask_app
from flaskext.mysql import MySQL

mysql = MySQL()
mysql.init_app(flask_app)


class UserDAO:

    def insertRegData(self,userVO):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "Insert into User(userName) values ('" + str(userVO.userName) + "')")
        dict1 = cursor.fetchall()
        print(dict1)
        conn.commit()
        cursor.close()
        conn.close()



