from flask_restful import Resource, reqparse
from models.user import User
from flask import request


parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be blank', required=True)
parser.add_argument('password', help='This field cannot be blank', required=True)


class GetToken(Resource):
    def post(self):
        data = parser.parse_args()
        response = User.get_token(data)
        return response


class AddUser(Resource):
    def post(self):
        data = parser.parse_args()
        if request.headers['token']:
            validate_admin = User.validate_token(request.headers['token'], True)
            if validate_admin:
                response = User.add_user(data)
                return response
            else:
                return {"status": "error", "code": 401,
                        "message": "Your role is not defined as Admin, you can't able to "
                                   "add user"}
        else:
            return {"status": "error", "code": 401, "message": "Token is required in headers."}
