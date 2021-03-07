FROM python:3.6-slim

RUN apt-get -y update
COPY ./requirements.pip /requirements.pip
RUN pip3.6 install --no-cache-dir -r /requirements.pip

COPY . /app

WORKDIR ./

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "3000"]