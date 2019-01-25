from datetime import datetime
from helpers.ConnectionHelper import ConnectionHelper
import bcrypt


class User:
    @staticmethod
    def get_token(data):
        cursor, db = ConnectionHelper.db_connect()
        query = "SELECT password,token FROM users where email = '{a}'".format(a=data['username'])
        response = None
        try:
            cursor.execute(query)
            result = cursor.fetchone()

            if len(result) > 0:
                password = data['password']
                if bcrypt.hashpw(password.encode('utf-8'), result[0]) == result[0]:
                    response = {"status": "success", "code": 200, "token": result[1]}
                else:
                    response = {"status": "error", "code": 401, "message": "Password doesn't match"}
            else:
                response = {"status": "error", "code": 401, "message": "User doesn't exist"}
        except Exception as e:
            response = {"status": "error", "code": 401, "message": "Exception : {a}".format(a=e)}
        finally:
            cursor.close()
            db.close()
            return response

    @staticmethod
    def add_user(data):
        response = None
        created_at = datetime.now()
        cursor, db = ConnectionHelper.db_connect()
        query = "INSERT INTO users (`name`,`email`,`password`,`role`,`token`,`created_at`) VALUES (%s,%s,%s,%s" \
                ",%s,%s)"

        name = data['username']
        email = data['username']
        password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
        role = 'employee'
        token = data['username']+data['password']+created_at.strftime('%d%m%Y%H%m%s')
        token = bcrypt.hashpw(token.encode('utf-8'), bcrypt.gensalt())

        try:
            cursor.execute(query, (name, email, password, role, token, created_at))
            db.commit()
            response = {"status": "success", "code": 200, "message": "User is added successfully"}
        except Exception as e:
            response = {"status": "error", "code": 401, "message": "Exception : {a}".format(a=e)}
        finally:
            cursor.close()
            db.close()
            return response

    @staticmethod
    def validate_token(token, admin=False, email=False):
        cursor, db = ConnectionHelper.db_connect()
        if admin:
            query = "SELECT email FROM users where token = '{a}' AND role = 'admin'".format(a=token)
        elif email:
            query = "SELECT email FROM users where token = '{a}' AND email = '{b}'".format(a=token, b=email)
        else:
            query = "SELECT email FROM users where token = '{a}'".format(a=token)
        response = None

        try:
            cursor.execute(query)
            result = cursor.fetchone()

            if len(result) > 0:
                response = True
            else:
                response = False
        except Exception as e:
            response = False
        finally:
            cursor.close()
            db.close()
            return response

    @staticmethod
    def get_user_ids(username=False):
        cursor, db = ConnectionHelper.db_connect()

        if username:
            query = "SELECT id, email FROM users where email = '{a}'".format(a=username)
        else:
            query = "SELECT id, email FROM users"
        response = {}

        try:
            cursor.execute(query)
            result = cursor.fetchall()

            if len(result) > 0:
                for row in result:
                    response[row[1]] = row[0]
        except Exception as e:
            response = {}
        finally:
            cursor.close()
            db.close()
            return response

