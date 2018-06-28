def db_access():
    
    conn = psycopg2.connect(host="localhost", databasee="postgres", user="postgres", password="XABC", port="5432")
    return conn.cursor()

@app.route("/rides", methods=['GET'])
def get_rides():
    pass
@app.route("/rides/<ride_Id>", methods=["GET"])
def add_ride(formData):
    pass
@app.route("/rides/<ride_Id>", methods=["GET"])
def delete_ride( ride_id):
    pass
@app.route('/users/rides/<rideid>/<requestid>',method=["PUT"] ) 
def add_user_to_ride(ride_id, requestid):
    pass
@app.route('/users/rides/<rideid>/<requestid>', method=["PUT"]) 
def reject_user_from_ride(ride_id, requestid):
    pass
