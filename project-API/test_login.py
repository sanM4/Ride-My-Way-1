from APP import app
import json

dt = {"username":"luqman", "email":"luqman@yahoo.com","password":"123abc"}
client = app.test_client()

def test_login():
        response = client.get('/api/v1/login')
        result = json.loads(response.data.decode())
        assert result["message"] == "logged in"
        assert response.status_code == 200

def test_register():
        response = client.post('/api/v1/register', data = json.dumps(dt) , content_type = 'application/json')
        result = json.loads(response.data.decode())
        assert result["username"] == "luqman"
        assert result["email"] == "luqman@yahoo.com"
        assert result["password"]== "123abc"
        assert response.status_code == 201
