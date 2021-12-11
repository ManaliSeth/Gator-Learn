from project import flask_app
from flaskext.mysql import MySQL

mysql = MySQL()
mysql.init_app(flask_app)


class UserDAO:

    def insertRegData(self,userVO):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("Select max(loginId) as loginId from Login")
        dict1 = cursor.fetchone()
        print(dict1)
        userVO.user_loginId = str(dict1[0])
        cursor.execute(
            "Insert into User(userName, user_loginId) values ('" + str(userVO.userName) + "', '" + str(userVO.user_loginId) + "')")
        dict1 = cursor.fetchall()
        print(dict1)
        conn.commit()
        cursor.close()
        conn.close()



