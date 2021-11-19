from project import *

# Database connection info. Note that this is not a secure connection.
flask_app.config['MYSQL_DATABASE_USER'] = 'admin'
flask_app.config['MYSQL_DATABASE_PASSWORD'] = 'aarshilp'
flask_app.config['MYSQL_DATABASE_DB'] = 'sfsu-tutoring-app'
flask_app.config['MYSQL_DATABASE_HOST'] = 'project-1.cxt6ynefb5sw.us-east-2.rds.amazonaws.com'



