
password = "qwerty"

class Config():
    SECRET_KEY = 'key'
    MYSQL_DATABASE_HOST = 'localhost'
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = password
    MYSQL_DATABASE_DB = 'project_schema'
    SQLALCHEMY_DATABASE_URI =   f"mysql://root:{password}@localhost/project_schema"
    SQLALCHEMY_TRACK_MODIFICATIONS = False