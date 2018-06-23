from APP import app
import json

def test_create_ride():
    """test that the API can fetch all rides available"""
    client = app.test_client()
    dt={"id": 6, "destination":"san francisco", "departure_point":"miami", "fare":1000, "driver":{"username":"amos"}}
    response = client.post('/api/v1/rides', data = json.dumps(dt) , content_type = 'application/json' )
    result = json.loads(response.data.decode())
    assert response.status_code == 201
    assert 'destination' in response.get_data(as_text=True)
    assert result['status'] == 'ok'
    assert result['destination'] =='san francisco'
    #assert isinstance(dat, list) == True
    #assert len(dat) == 3
    #assertEqual(data['count'], 0)
    #assertIsInstance(data['count'], int)
    #assertEqual(data['previous'], None)
    #assertEqual(data['next'], None)

#def test_invalid_JSON(self):
    #"""Test status code 405 from improper JSON on post to raw"""
    #client = app.test_client()
    #res = client.post('/api/v1/rides', data="This isn't a json... it's a string!")
    
    #assert res.status_code == 405