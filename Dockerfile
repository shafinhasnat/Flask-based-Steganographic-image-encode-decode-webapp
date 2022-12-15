FROM ubuntu:18.04
WORKDIR /usr/src
ENV LANG C.UTF-8
RUN apt-get -y update
RUN apt-get -y install python3.6 python3-pip
RUN apt-get install -y libsm6 libxext6 libxrender-dev
RUN apt-get -y install libpq-dev
RUN pip3 install -r requirements.txt
EXPOSE 8080
CMD gunicorn --bind 0.0.0.0:8080 app:app -w 4