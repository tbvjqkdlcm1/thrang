import os

BASE_DIR = os.path.dirname(__file__)

aws_db = {
    "user": "admin",
    "password": "criticalc",
    "host": "database-3.cxbibmlxmmra.us-west-2.rds.amazonaws.com",
    "port": "3306",
    "database": "mac",
}

SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{aws_db['user']}:{aws_db['password']}@{aws_db['host']}:{aws_db['port']}/{aws_db['database']}?charset=utf8"
SQLALCHEMY_TRACK_MODIFICATIONS = 1