FROM python:3.9
RUN apt-get update -y
RUN apt-get upgrade -y

WORKDIR /

COPY ./DjangoNewsAndGeo/requirements.txt ./DjangoNewsAndGeo
RUN pip install -r /DjangoNewsAndGeo/requirements.txt
COPY ./DjangoNewsAndGeo ./DjangoNewsAndGeo

CMD [ "py", "./DjangoNewsAndGeo/manage.py", "runserver", "0.0.0.0:8080"]
