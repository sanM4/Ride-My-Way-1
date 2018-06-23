from APP import app

def test_app_runs():
    """test that app runs"""
    client = app.test_client()
    res = client.get('/api/v1/rides')
    assert res.status_code == 200
