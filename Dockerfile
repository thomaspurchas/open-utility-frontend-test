# Inspiration from:
# https://hub.docker.com/r/frolvlad/alpine-python3/~/dockerfile/
# https://github.com/docker/labs/blob/master/beginner/flask-app/Dockerfile

FROM alpine:3.15

RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    pip3 install --upgrade pip

COPY requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt

COPY *.py /usr/src/app/
COPY templates/ /usr/src/app/templates/
COPY static/ /usr/src/app/static/

WORKDIR usr/src/app/

# tell the port number the container should expose
EXPOSE 5000

CMD ["python3", "/usr/src/app/weather_server.py"]