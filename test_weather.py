from weather import Weather, whats_the_weather_like, whats_the_weather_like_from_string

def test_names():
    rain = Weather('rain')
    sun = Weather('sun')
    assert str(rain) == 'Rain'
    assert str(sun) == 'Sun'

def test_eq():
    assert Weather('sun') == Weather('sun')

def test_commutative():
    weather1 = Weather('sun') + Weather('rain')
    weather2 = Weather('rain') + Weather('sun')

    assert weather1 == weather2

def test_sum():
    rain = Weather('rain')
    sun = Weather('sun')

    added = rain + sun
    assert str(added) == 'Sun, Rain'
    assert added.emoji == '🌈'

def test_sub():
    rain = Weather('rain')
    sun = Weather('sun')

    added = rain + sun
    assert str(added) == 'Sun, Rain'

    subed = added - rain
    assert str(subed) == 'Sun'
    assert subed == sun

def test_date_weather():
    dates = {
        '2017/01/07': 'Wind',
        '2017/01/09': 'Sun',
        '2017/01/12': 'Sun, Rain',
        '2017/01/01': 'Overcast'
    }

    for date, weather in dates.items():
        assert whats_the_weather_like_from_string(date) == weather