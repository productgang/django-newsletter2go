FROM ubuntu:14.04
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN apt-get install -y python python-dev python-pip python-virtualenv software-properties-common python-software-properties
RUN add-apt-repository ppa:fkrull/deadsnakes
RUN apt-get update
RUN apt-get install -y python2.7 python3.3 python3.4
RUN mkdir /code
WORKDIR /code
ADD requirements-test.txt /code/
RUN pip install -r requirements-test.txt
ADD . /code/
