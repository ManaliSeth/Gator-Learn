# Credentials Folder

## The purpose of this folder is to store all credentials needed to log into your server and databases. This is important for many reasons. But the two most important reasons is 
    1. Grading , servers and databases will be logged into to check code and functionality of application. Not changes will be unless directed and coordinated with the team.
    2. Help. If a class TA or class CTO needs to help a team with an issue, this folder will help facilitate this giving the TA or CTO all needed info AND instructions for logging into your team's server. 


# Below is a list of items required. Missing items will causes points to be deducted from multiple milestone submissions.

1. Server URL or IP : http://3.144.136.131; (Private IPv4 address) 172.31.34.200
2. SSH username : ubuntu
3. SSH password or key: SSH key (.pem)/(.ppk for PuTTy) uploaded
    <br> If a ssh key is used please upload the key to the credentials folder.
4. Database URL or IP and port used: Hostname - se-tutoring-database.cxt6ynefb5sw.us-east-2.rds.amazonaws.com, Port - 3306
5. Database username : admin
6. Database password : admin123
7. Database name (basically the name that contains all your tables) : se_tutoring
8. Instructions on how to use the above information: Database can be accessed using MySQL Workbench.
    <br> (Using PuTTy to SSH into instance) Upon opening PuTTy, the configuration page opens in the Session category. Add public IPv4 (3.144.136.131) in Host name and upload .ppk file in Auth under SSH tab in Connections. Click on open and put username as ubuntu for login. 
    <br> Whenever we restart the instance, follow the commands as below:
    <br> Move to the following directory using cd command:  cd hosting
    <br> 1) export FLASK_APP="main.py"
    <br> 2) flask run --host=0.0.0.0 --port=8000
    <br> The application can then be run on remote host in browser via http://3.144.136.131:8000/
    
# Most important things to Remember
## These values need to kept update to date throughout the semester. <br>
## <strong>Failure to do so will result it points be deducted from milestone submissions.</strong><br>
## You may store the most of the above in this README.md file. DO NOT Store the SSH key or any keys in this README.md file.
