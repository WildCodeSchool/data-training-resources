FROM python:3.10.0-slim-buster

WORKDIR /django_to_gcp_app

COPY requirements.txt requirements.txt

RUN pip3 install  -r requirements.txt

COPY . .

CMD [ "python3", "app.py" ]