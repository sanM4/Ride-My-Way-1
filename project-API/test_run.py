from APP import app

def test_app_runs():
    """test that app runs"""
    client = app.test_client()
    res = client.get('/rides')
    assert res.status_code == 200
