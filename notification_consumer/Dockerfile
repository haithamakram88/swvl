FROM python:3.6-slim

RUN apt-get -y update
COPY ./requirements.pip /requirements.pip
RUN pip3.6 install --no-cache-dir -r /requirements.pip

COPY . /app/notification_consumer
COPY main.py /app

WORKDIR ./app

CMD python3 main.py
