import datetime
from collections import namedtuple
from operator import attrgetter

import prime

# Use a prime sieve to calculate all primes up 31. Then is super easy to check primeness
# assuming that no one changes the number of days in a month.
PRIMES = prime.sieve(31)

class Weather():
    WeatherType = namedtuple('WeatherType', ['name', 'emoji', 'order'])

    SUN = WeatherType('Sun', '☀️', 0)
    RAIN = WeatherType('Rain', '🌧️', 1)
    WINDY = WeatherType('Windy', '💨', 2)
    CLOUDY = WeatherType('Cloudy', '☁️', 3)
    OVERCAST = WeatherType('Overcast', '⛅️', 4)

    weather_mapping = {
        w.name.lower(): w for w in [SUN, RAIN, WINDY, CLOUDY, OVERCAST]
    }

    emoji_combinations = {
        '🌈': {RAIN, SUN},
        '☀️🔥😡': {OVERCAST, SUN},
        '☀️🔥😡': {CLOUDY, SUN},
        '💨☂️': {RAIN, WINDY}
    }

    def __init__(self, weather):
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

    @classmethod
    def from_types(cls, weather_types):
        weather = cls(cls.RAIN.name)
        weather.weather = weather_types
        return weather

    def sorted_weather(self):
        return sorted(list(self.weather), key=attrgetter('order'))

    @property
    def emoji(self):
        output = ''
        weather = self.weather.copy()
        for emoji, combo in self.emoji_combinations.items():
            if combo.issubset(weather):
                output += emoji
                weather -= combo
        
        output += ''.join([w.emoji for w in weather])
        return output

