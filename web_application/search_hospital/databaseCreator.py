from .mySQLDB import MySQLDB
from .oracleDB import OracleDB


class DatabaseCreator:
    def getDatabase(database):
        if database == "mysql":
            return MySQLDB()
        if database == "oracle":
            return OracleDB()


