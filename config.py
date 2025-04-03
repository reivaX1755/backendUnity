import os

class Config:
    MYSQL_HOST = os.getenv("DB_HOST", "mysql-bdplataformas2d.alwaysdata.net")
    MYSQL_USER = os.getenv("DB_USER", "407653")
    MYSQL_PASSWORD = os.getenv("DB_PASS", "administrador123456789.")
    MYSQL_PORT = int(os.getenv("DB_PORT", 3306))
    MYSQL_DATABASE = os.getenv("DB_NAME", "bdplataformas2d_connect")
