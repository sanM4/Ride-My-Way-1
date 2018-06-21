from APP.API import Bluep

import json

from flask import request, jsonify, make_response


def ride_resource():
    """implement ride resource as a list of dictionary"""
    rides = [{"id":1, "destination":"Nairobi", "departure_point":"Eldoret", "fare":800, "driver":{"username":"Jesse", "gender":"male"},
 "passengers":{"usernames":["jane", "jack", "frank"],"number":3}, "stop_over":["Nakuru","Limuru"]}, {"id":2, "destination":"Mombasa", "departure_point":"Nairobi", "fare":1200, "driver":{"username":"Milac", "gender":"female"},
"passengers":{"usernames":["jeff", "steve"],"number":2}, "stop_over":["Mtito Andei"]}] 
    return rides

@Bluep.route('/api/v1/rides', methods=['GET'])
def get_rides():
    """get all ride"""
    return make_response(jsonify(ride_resource()))


@Bluep.route('/api/v1/rides', methods=['POST'])
def create_ride(): 
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = data['password']
    return make_response(jsonify({
                                 "status": "ok",
                                 "username": username , 
                                 "email": email, 
                                 "password": password
                                 }), 201)


@Bluep.route('/rides/<int:id>/driver', methods=['GET'])
def get_driver(id):
    pass

@Bluep.route('/rides/<int:id>', methods=['POST'])
def request_user(id):
    pass

