FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 0
RUN apt-get update
RUN apt-get -y install default-libmysqlclient-dev gcc

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]