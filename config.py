import os
from ButterSalt import app

DEBUG = True
SALT_API = 'http://192.168.1.71:8000'
USERNAME = 'test'
PASSWORD = 'test'
SECRET_KEY = os.urandom(24)
SQL = os.path.join(app.root_path, '../database/schema.sql')
DATABASE = os.path.join(app.root_path, '../database/schema.db')