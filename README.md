# Setting up

Setting this up is pretty simple, there are two methods Docker and VirtualEnv

## Docker

Docker is the easiest, assuming that you already have [Docker installed](https://docs.docker.com/engine/installation/).

From within this repo run:

```
docker build -t docker build -t thomas-forecast-challenge .
```

then run:

```
docker run -p 5000:5000 thomas-forecast-challenge
```

Finally head over to http://127.0.0.1:5000

To run the tests, run:

```
docker run thomas-forecast-challenge pytest
```

## VirtualEnv

I'm gonna assume you can create a VirtualEnv without any help. Once you have done that run:

```
pip3 install -r requirements.txt
```

To launch the server run:

```
python3 weather_server.py
```

Finally head over to http://127.0.0.1:5000

To run the tests, run:

```
pytest
```