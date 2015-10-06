FROM ubuntu:14.04

MAINTAINER Victor and Kaisa

RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip build-essential libpq-dev libxml2-dev libxslt1-dev git libffi-dev libproj-dev gdal-bin

COPY . /srv

WORKDIR /srv

RUN git clone https://github.com/vmenezes/identity-toolkit-python-client.git
RUN pip3 install identity-toolkit-python-client
RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD gunicorn wsgi:application

