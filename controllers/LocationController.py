from flask_restful import Resource, reqparse
from models.location import Location
from models.user import User
from flask import request

parser = reqparse.RequestParser()


class UpdateLocation(Resource):
    @staticmethod
    def post():
        parser.add_argument('json_data', help='This field cannot be empty', required=True)

        if 'token' in request.headers:
            validate = User.validate_token(request.headers['token'])
            if validate:
                data = parser.parse_args()
                response = Location.insert_data(data)
                return response
            else:
                return {"status": "error", "code": 401, "message": "Token Mismatched."}
        else:
            return {"status": "error", "code": 401, "message": "Token is required in headers."}


class GetLocation(Resource):
    @staticmethod
    def post():
        if 'token' in request.headers:
            parser.add_argument('emp_email', help='This field cannot be empty', required=True)
            data = parser.parse_args()
            validate_admin = User.validate_token(request.headers['token'], True)
            if validate_admin:
                response = Location.get_locations(data)
            else:
                validate = User.validate_token(request.headers['token'], False, data['emp_email'])
                if validate:
                    response = Location.get_locations(data)
                else:
                    response = {"status": "success", "code": 200, "message": "Either Token Mismatched or token of "
                                                                             "respective email not matched."}
            return response
        else:
            return {"status": "error", "code": 401, "message": "Token is required in headers."}
