import os

class Config:
    MYSQL_HOST = os.getenv("DB_HOST", "130.162.54.212")
    MYSQL_USER = os.getenv("DB_USER", "freedb_unityquestdb_admin")
    MYSQL_PASSWORD = os.getenv("DB_PASS", "bNzQ@rYgFb2tqga")
    MYSQL_PORT = int(os.getenv("DB_PORT", 3306))
    MYSQL_DATABASE = os.getenv("DB_NAME", "freedb_unityquestdb")
