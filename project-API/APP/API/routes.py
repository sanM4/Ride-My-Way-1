from APP.API import Bluep
import json
from flask import request, jsonify, make_response

def ride_resource():
    """implement ride resource as a list of dictionary"""
    rides = [{"id":1, "destination":"Nairobi", "departure_point":"Eldoret", "fare":800, "driver":{"username":"Jesse", "gender":"male"}, "requests":[{"username":"jane","state":"accepted"},{"username":"jack","state":"accepted"},{"username":"frank", "state":"accepted"}],
 "passengers":{"usernames":["jane", "jack", "frank"],"number":3}, "stop_over":["Nakuru","Limuru"]}, {"id":2, "destination":"Mombasa", "departure_point":"Nairobi", "fare":1200, "driver":{"username":"Milac", "gender":"female"},
"passengers":{"usernames":["jeff", "steve"],"number":2}, "stop_over":["Mtito Andei"]}] 
    return rides

@Bluep.route('/rides', methods=['GET'])
def get_rides():
    """get all ride"""
    return make_response(jsonify(ride_resource()))

@Bluep.route('/rides/<int:id>', methods=['GET'])
def get_user(id):
    """get ride by id"""
    for ride in ride_resource():
        if ride["id"] == id:
            return make_response(jsonify(ride))

@Bluep.route('/rides/<int:id>', methods=['PUT'])
def update_ride_requests(id):
    """update ride by id"""
    for ride in ride_resource():
       if ride["id"] == id:
           data=request.get_json()
           ride["requests"].append(data)
           return make_response(jsonify(ride), 201)

@Bluep.route('/rides', methods=['POST'])
def create_ride():
  """create ride"""
    data = request.get_json()
    id = data['id']
    destination = data['destination']
    departure_point = data['departure_point']
    fare = data['fare']
    driver = data['driver']
    return make_response(jsonify({"results":"success",
                                 "status": "ok",
                                 "id": id , 
                                 "destination": destination, 
                                 "fare": fare,
                                 "driver":driver}), 201)

