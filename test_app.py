import app

def test_record_login():
    response = app.record_login({'data': {'from': 'pytest'}})
    assert 200 <= response.status_code < 300

def test_invalid_token():
    response = app.validate('SOME_INVALID_TOKEN')
    assert response.status_code == 403