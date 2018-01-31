"""
Unit tests for weather server.
"""

import json

import pytest
from flask import url_for

from weather_server import app as APP

@pytest.fixture
def app():
    """Return Flask app"""

    return APP

def test_basic_get(client):
    """Test correct response to basic GET request"""

    res = client.get(url_for('forcast', date_string='2017/01/07'))

    assert res.status_code == 200
    assert 'Wind' in str(res.data)

def test_json_post(client):
    """Test correct response to JSON POST request"""

    data = ["2017/01/03", "2017/03/14", "2017/03/15", "2017/07/24"]

    res = client.post(url_for('forcast_many'), data=json.dumps(data))

    assert res.json == {
        "2017/01/03": "Sun, Wind",
        "2017/03/14": "Rain",
        "2017/03/15": "Overcast",
        "2017/07/24": "Sun, Rain"
    }

def test_json_emoji_post(client):
    """Test correct response to emoji JSON POST request"""

    data = ["2017/01/03", "2017/03/14", "2017/03/15", "2017/07/24"]

    res = client.post(url_for('forcast_many_emoji'), data=json.dumps(data))

    assert res.json == {
        "2017/01/03": "☀️💨",
        "2017/03/14": "🌧️",
        "2017/03/15": "⛅️",
        "2017/07/24": "🌈"
    }
