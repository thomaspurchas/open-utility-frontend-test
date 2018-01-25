import datetime

from flask import Flask, Response, request, jsonify

from weather import whats_the_weather_like

DATE_FORMAT = '%Y/%m/%d'

app = Flask(__name__)

def parse_date(date_string):
    return datetime.datetime.strptime(date_string, DATE_FORMAT)

@app.route("/")
@app.route("/forcast/")
def hello():
    return Response("This is not the weather you're looking for...", status=404)

@app.route('/forcast/<path:date_string>')
def forcast(date_string):
    date_string = date_string.strip('/')

    try:
        date = parse_date(date_string)
    except ValueError:
        return Response("You might want to double check your date</br>I accept 'YYYY/MM/DD' and Earl Grey", status=418)

    weather = whats_the_weather_like(date)

    return '{}</br>{}'.format(str(weather), weather.emoji())

@app.route('/forcast/', methods=['POST'])
def forcast_many():
    dates = request.get_json(force=True)

    response = {}
    for date in dates:
        try:
            response[date] = str(whats_the_weather_like(parse_date(date)))
        except ValueError:
            res = jsonify(error="Unable to handle date '{}'".format(date))
            res.status_code = 400
            return res

    return jsonify(response)