#!/usr/bin/env python3

import datetime

from flask import Flask, Response, request, jsonify, abort, render_template

from weather import whats_the_weather_like

DATE_FORMAT = '%Y/%m/%d'

app = Flask(__name__)

def parse_date(date_string):
    return datetime.datetime.strptime(date_string, DATE_FORMAT)

@app.route("/")
def hello():
    return render_template('hello.html')

@app.route("/forcast/")
def woops():
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

def get_weather_forcast(dates):
    response = {}
    for date in dates:
        try:
            response[date] = whats_the_weather_like(parse_date(date))
        except ValueError:
            res = jsonify(error="Unable to handle date '{}'".format(date))
            res.status_code = 400
            abort(res)

    return response

@app.route('/forcast/', methods=['POST'])
def forcast_many():
    dates = request.get_json(force=True)

    res = get_weather_forcast(dates)
    res = {d: str(w) for d, w in res.items()}

    return jsonify(res)

@app.route('/forcast/emoji/', methods=['POST'])
def forcast_many_emoji():
    dates = request.get_json(force=True)

    res = get_weather_forcast(dates)
    res = {d: w.emoji() for d, w in res.items()}

    return jsonify(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)