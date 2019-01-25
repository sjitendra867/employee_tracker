import pymysql


class ConnectionHelper:
    @staticmethod
    def db_connect():
        try:

            host = "localhost"
            user = "root"
            password = "password"
            database = "emp_tracker"

            db = pymysql.connect(host, user, password, database)
            cursor = db.cursor()
            return cursor, db

        except Exception as e:
            return "Exception : {a}".format(a=e)
