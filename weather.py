import datetime
from collections import namedtuple
from operator import attrgetter

import prime

# Use a prime sieve to calculate all primes up 31. Then is super easy to check primeness
# assuming that no one changes the number of days in a month.
PRIMES = prime.sieve(31)

class Weather():
    '''
    Weather object that lets you do some basic weather maths. It provides addition and subtraction
    operations, addition is commutative, subtraction is not. The basic weather types have fixed order
    so that string representations of combined weather is always the same e.g.

    Weather('sun') + Weather('rain') == "Sun, Rain"
    Weather('rain') + Weather('sun') == "Sun, Rain"
    '''

     # Use named tuples to create basic weather types with associated emoji and order
    WeatherType = namedtuple('WeatherType', ['name', 'emoji', 'order'])

    SUN = WeatherType('Sun', '☀️', 0)
    RAIN = WeatherType('Rain', '🌧️', 1)
    WIND = WeatherType('Wind', '💨', 2)
    CLOUD = WeatherType('Cloud', '☁️', 3)
    OVERCAST = WeatherType('Overcast', '⛅️', 4)

    # Create a mapping object so that we can quickly lookup basic weather types
    weather_mapping = {
        w.name.lower(): w for w in [SUN, RAIN, WIND, CLOUD, OVERCAST]
    }

    # Create some emoji weather combination substitutes so emoji is better
    emoji_combinations = {
        '🌈': {RAIN, SUN},
        '☀️🔥😡': {OVERCAST, SUN},
        '☀️🔥😡': {CLOUD, SUN},
        '💨☂️': {RAIN, WIND}
    }

    def __init__(self, weather):
        if weather is None:
            self.weather = set()
        else:
            self.weather = {self.weather_mapping[weather.lower()]}
        

    def __add__(self, b):
        if b is None:
            return self

        return Weather.from_types(self.weather.union(b.weather))

    def __sub__(self, b):
        if b is None:
            return self

        return Weather.from_types(self.weather - b.weather)

    def __eq__(self, b):
        return self.weather == b.weather

    def __str__(self):
        return ', '.join([w.name for w in self.sorted_weather()])

    def emoji(self):
        output = ''
        weather = self.weather.copy()
        for emoji, combo in self.emoji_combinations.items():
            if combo.issubset(weather):
                output += emoji
                weather -= combo
        
        output += ''.join([w.emoji for w in weather])
        return output

    @classmethod
    def from_types(cls, weather_types):
        weather = cls(None)
        weather.weather = weather_types
        return weather

    def sorted_weather(self):
        return sorted(list(self.weather), key=attrgetter('order'))


def whats_the_weather_like(date):
    weather = Weather(None)
    if date.day % 2 == 0:
        weather += Weather('Rain')
    if date.day in PRIMES:
        weather += Weather('Wind')
    if (date.day % 3 == 0) != (date.day % 5 == 0):
        weather += Weather('Sun')
    if weather == Weather(None):
        weather = Weather('Overcast')

    return weather

def whats_the_weather_like_from_string(date):
    '''
    Tells you what the weather is like on a date provided 
    as a string in YYYY/MM/DD format
    '''

    parsed_datetime = datetime.datetime.strptime(date, '%Y/%m/%d')

    weather = whats_the_weather_like(parsed_datetime.date())
    return str(weather)
