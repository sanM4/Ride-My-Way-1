from APP import app
import json

def test_create_ride():
    """test that the API can fetch all rides available"""
    client = app.test_client()
    res = client.post('/api/v1/rides', data={"todo_text": "do something useful"})
    assert res.status_code == 200
    assert 'do something useful' in res.get_data(as_text=True)
    #assert data['status'] == 'success'
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