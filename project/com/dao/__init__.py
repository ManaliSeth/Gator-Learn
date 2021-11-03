from project import *
import pymysql
#
# def conn_db():
#     return pymysql.connect(
#         host='localhost',
#         user='root',
#         password='Team4@2021',
#         db='se_tutoringservices',
#         cursorclass=pymysql.cursors.DictCursor,
#         use_unicode = True,
#         charset = "utf8"
#     )

# Database connection info. Note that this is not a secure connection.
flask_app.config['MYSQL_DATABASE_USER'] = 'admin'
flask_app.config['MYSQL_DATABASE_PASSWORD'] = 'aarshilp'
flask_app.config['MYSQL_DATABASE_DB'] = 'sfsu-tutoring-app'
flask_app.config['MYSQL_DATABASE_HOST'] = 'project-1.cxt6ynefb5sw.us-east-2.rds.amazonaws.com'



