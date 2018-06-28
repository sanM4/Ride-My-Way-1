def db_access():
    conn = psycopg2.connect(host="localhost", databasee="postgres", user="postgres", password="XABC", port="5432")
    return conn.cursor()

def test_get_allrides():
    query = "SELECT * FROM rideoffers"
    rides = db_access().execute(query)
    if rides:
        return {'status': 'sucsess', 'rides': rides}
    return {'status': False}

def test_add_ride():
    query = "INSERT INTO rideoffers (ridecreator, destination, departure, date, fare,) VALUES (:ridecreator :destination, :departure, :date, :fare)"
    data = {
            "ridecreator": formData['ridecreator'],
            "destination": formData['destination'],
            "date": parser.parse(form['date']),
            "fare": formData['fare'],
            "departure": formData['departure']
    }
    ride = db_access().execute(query, data)
    if ride:
        return {'status': 'sucess', 'driver': ride["ridecreator"]}
    return {'status': False}

def test_deleyer(ride_id):
    query = "SELECT * FROM rideoffers WHERE rideid = :ride_id"
    data = {
            "rideid": ride_id
    }
    ride=db_access().execute(query, data)
    if ride:
        query = "DELETE FROM rides WHERE rideid = :ride_id"
        result=db_access().evaluate(query, data)

        return {'status': 'sucess', 'result'}
    return {'status': False}

def test_add_user():
   query = "SELECT rideid, requests FROM rideoffers WHERE rideid = :ride_id AND requestid = ANY (requests)"
    data = {
            "requestid": requestid,
            "ride_id": ride_id
        }
    db_access().execute(query, data)
    if not result:
        query = "INSERT INTO rideoffers(requests) wHERE rideid= :ride_id VALUES (:requestid)"
        db_acess().execute(query, data)
    return {'status': True, 'result': result}     
def test_reject():
    query = "SELECT * FROM rideoffers WHERE rideid = :ride_id"
    data = {
            "requestid": requestid,
            "ride_id": ride_id
        }
    db_access().execute(query, data)
    if result:
        query = "DELETE requestid FROM rideoffers WHERE  rideid= :ride_id AND requestid= :requestid
        db_access().execute(query, data)
        return {'status': "Success"}
    return {'status': False}
