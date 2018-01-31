"""
Unit tests for Weather object.
"""

from weather import Weather, whats_the_weather_like_from_string

def test_names():
    """Test that names of weather work"""

    rain = Weather('rain')
    sun = Weather('sun')
    assert str(rain) == 'Rain'
    assert str(sun) == 'Sun'

def test_eq():
    """Test that weather equality works"""

    assert Weather('sun') == Weather('sun')

def test_commutative():
    """Test that weather addition is commutative"""

    weather1 = Weather('sun') + Weather('rain')
    weather2 = Weather('rain') + Weather('sun')

    assert weather1 == weather2
    assert str(weather1) == str(weather2)

def test_sum():
    """Test that weather addition result in correct compound weather and emoji"""
    rain = Weather('rain')
    sun = Weather('sun')

    added = rain + sun
    assert str(added) == 'Sun, Rain'
    assert added.emoji() == '🌈'

def test_sub():
    """Test weather substraction works"""

    rain = Weather('rain')
    sun = Weather('sun')

    added = rain + sun
    assert str(added) == 'Sun, Rain'

    subed = added - rain
    assert str(subed) == 'Sun'
    assert subed == sun

def test_weather_priority():
    """Test basic weather priorities produce deterministic compound weathers"""

    sun = Weather('sun')
    wind = Weather('wind')

    w1 = wind + sun
    w2 = sun + wind

    assert str(w1) == str(w2) == 'Sun, Wind'
    assert w1.emoji() == w2.emoji() == '☀️💨'


def test_date_weather():
    """Test that we get the correct weather on certain dates"""

    dates = {
        '2017/01/07': 'Wind',
        '2017/01/09': 'Sun',
        '2017/01/12': 'Sun, Rain',
        '2017/01/01': 'Overcast'
    }

    for date, weather in dates.items():
        assert whats_the_weather_like_from_string(date) == weather
