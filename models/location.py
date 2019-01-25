from datetime import datetime
from helpers.ConnectionHelper import ConnectionHelper
import json
from models.user import User
from helpers.LocationHelper import LocationHelper


class Location:
    @staticmethod
    def insert_data(data):
        response = None
        cursor, db = ConnectionHelper.db_connect()
        try:
            users = User.get_user_ids()
            data = json.loads(data['json_data'])
            created_at = datetime.now()
            query = "INSERT INTO locations (`user_id`,`date`,`source`,`source_lat`,`source_long`,`destination`," \
                    "`destination_lat`,`destination_long`,`distance_km`,`created_at`) VALUES (%s,%s,%s,%s" \
                    ",%s,%s,%s,%s,%s,%s)"

            data_list = []

            for row in data:
                source = LocationHelper.get_location(row['source_lat'], row['source_long'])
                destination = LocationHelper.get_location(row['destination_lat'], row['destination_long'])
                distance = LocationHelper.get_distance(row['source_lat'], row['source_long'], row['destination_lat'],
                                                       row['destination_long'])

                data_list.append((users[row['email']], row['date'], source, row['source_lat'], row['source_long'],
                                  destination, row['destination_lat'], row['destination_long'], distance, created_at),)

                cursor.executemany(query, data_list)
                db.commit()
                response = {"status": "success", "code": 200, "message": "Tracks added successfully"}
        except Exception as e:
            db.rollback()
            response = {"status": "error", "code": 401, "message": "Exception : {a}".format(a=e)}
        finally:
            cursor.close()
            db.close()
            return response

    @staticmethod
    def get_locations(data):
        cursor, db = ConnectionHelper.db_connect()
        response = None
        try:
            user = User.get_user_ids(data['emp_email'])
            if len(user) and user[data['emp_email']]:
                user_id = user[data['emp_email']]
                if 'from_date' in data and 'to_date' in data:
                    query = "SELECT date, CONCAT(source,' - ', destination) as route, distance_km FROM locations where " \
                            "user_id = '{a}' AND date BETWEEN '{b}' AND '{c}' ORDER BY date ASC"\
                        .format(a=user_id, b=data['from_date'].strftime('%Y-%m-%d'),
                                c=data['to_date'].strftime('%Y-%m-%d'))
                else:
                    query = "SELECT date, CONCAT(source,' - ', destination) as route, distance_km FROM locations " \
                            "where user_id = '{a}' ORDER BY date DESC LIMIT 1".format(a=user_id)
                cursor.execute(query)
                result = cursor.fetchall()

                if len(result) > 0:
                    data_list = []
                    for row in result:
                        data_list.append({
                            "date": row[0].strftime('%d-%m-%Y'),
                            "route": row[1],
                            "distance": str(round(row[2], 2)) +" Km"
                        })
                    response = {"status": "success", "code": 200, "data": data_list}
                else:
                    response = {"status": "success", "code": 200, "message": "Data not found."}
            else:
                response = {"status": "success", "code": 200, "message": "User not matched with our Records."}
        except Exception as e:
            db.rollback()
            response = {"status": "error", "code": 401, "message": "Exception : {a}".format(a=e)}
        finally:
            cursor.close()
            db.close()
            return response
