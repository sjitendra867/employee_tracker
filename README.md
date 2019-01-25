##Required libraries:(python version 3.6)

pip3 install virtualenv
sudo apt-get install virtualenv
pip3 install bcrypt
pip3 install datetime 
pip3 install reverse_gecoder
pip3 install geopy
pip3 install pymysql
pip3 install json

##After git clone of repository:
cd emp_tracker
virtualenv venv
venv/bin/activate
pip3 install Flask
pip3 install Flask-RESTful 

##API Descriptions :-

Base URL :- As of now base URL is http://localhost:5000/
Username: admin@gmail.com
Pass:  admin123

#get-token :-
  
URL : http://localhost:5000/get-token
Request Type : POST
Content-Type : application/json
Request Parameters
{
	"username":"admin@gmail.com", 
	"password":"admin123"
}
Response Example
{
    "status": "success",
    "code": 200,
    "token": "$2b$12$MlXtcOsiCmh2GgC.I51vneTL8Nrdaio.zzP1Q1m8KqV7WRlFUv08i"
}



##Note :- For all remaining API calls you need to pass the access_token in request header in token field. 
#For example :- 
#In REQUEST HEADER
token : $2y$10$hOaLmxAigjGSkPylf9z3LuWFlRuq0fahvEy9.zQnMMryPtrD3WNei



#add-user :-
  
URL : http://localhost:5000/add-user
Request Type : POST
Content-Type : application/json
Request Parameters
{
	"username":"emp5@gmail.com", 
	"password":"emp231"
}
Response Example
{
    "status": "success",
    "code": 200,
    "message": "User is added successfully"
}


#add-tracks :-
  
URL
http://localhost:5000/add-tracks
Request Type : POST
Content-Type : application/json
Request Parameters
{
    "Json_data":
    [
        {
            "email":"employee@gmail.com",
            "date":"2019-01-24",
            "source_lat":"26.8467",
            "source_long":"80.9462",
            "destination_lat":"26.4499",
            "destination_long":"80.3319"
        },
        {
            "email":"emp3@gmail.com",
            "date":"2019-01-24",
            "source_lat":"26.8467",
            "source_long":"80.9462",
            "destination_lat":"26.4499",
            "destination_long":"80.3319"
        }
    ]
}
Response Example
{
    "status": "success",
    "code": 200,
    "message": "Track added successfully"
}

#get-tracks :-
  
URL : http://localhost:5000/get-tracks
Request Type : POST
Content-Type : application/json
Request Parameters
{
	"emp_email":"employee@gmail.com", 
	"from_date":"2019-01-24",
	"to_date":"2019-01-24",
}
##NOTE:from_date & to_date is optional parameter


Response Example
{
    "status": "success",
    "code": 200,
    "data": 
    [
        {
            "date": "24-01-2019",
            "route": "Lucknow, Uttar Pradesh - Kanpur, Uttar Pradesh",
            "distance": "75.32 Km"
        }
    ]
}
