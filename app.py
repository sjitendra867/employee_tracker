from flask import Flask
from flask_restful import Api
import controllers.UserController as UserController
import controllers.LocationController as LocationController

app = Flask(__name__)
api = Api(app)

api.add_resource(UserController.GetToken, '/get-token')
api.add_resource(UserController.AddUser, '/add-user')
api.add_resource(LocationController.UpdateLocation, '/add-tracks')
api.add_resource(LocationController.GetLocation, '/get-tracks')

if __name__ == '__main__':
   app.run()
