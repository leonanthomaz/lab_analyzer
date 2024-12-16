import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'mysql+pymysql://root:leonan2knet@localhost:3306/labanalyzer')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
