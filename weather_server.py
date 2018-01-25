import datetime

from flask import Flask, abort, Response

from weather import whats_the_weather_like

DATE_FORMAT = '%Y/%m/%d'

app = Flask(__name__)

@app.route("/")
@app.route("/forcast/")
def hello():
    return Response("This is not the weather you're looking for...", status=404)

@app.route('/forcast/<path:date_string>')
def forcast(date_string):
    date_string = date_string.strip('/')

    try:
        date = datetime.datetime.strptime(date_string, DATE_FORMAT)
    except ValueError:
        return Response("You might want to double check your date</br>I accept 'YYYY/MM/DD' and Earl Grey", status=418)

    weather = whats_the_weather_like(date)

    return '{}</br>{}'.format(str(weather), weather.emoji())
