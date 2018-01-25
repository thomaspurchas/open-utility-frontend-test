import json

import pytest
from flask import url_for

from weather_server import app as APP

@pytest.fixture
def app():
    return APP

def test_basic_get(client):
    res = client.get(url_for('forcast', date_string='2017/01/07'))

    assert res.status_code == 200
    assert 'Wind' in str(res.data)

def test_json_post(client):
    data = ["2017/01/03", "2017/03/14", "2017/03/15", "2017/07/24"]

    res = client.post(url_for('forcast_many'), data=json.dumps(data))

    assert res.json == {
        "2017/01/03": "Sun, Wind",
        "2017/03/14": "Rain",
        "2017/03/15": "Overcast",
        "2017/07/24": "Sun, Rain"
    }