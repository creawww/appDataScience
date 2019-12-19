FROM python:3.7-stretch

COPY ./app/requirements.txt /
RUN pip3 install -r requirements.txt

WORKDIR /home/app

EXPOSE 5000
