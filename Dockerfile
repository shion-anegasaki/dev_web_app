FROM ubuntu:18.04
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive

RUN sed -i.bak -e "s%http://archive.ubuntu.com/ubuntu/%http://ftp.iij.ad.jp/pub/linux/ubuntu/archive/%g" /etc/apt/sources.list
RUN apt update
RUN apt install -y build-essential libssl-dev libffi-dev libmysqlclient-dev 
RUN apt install -y python3 python3-pip python3-dev

RUN pip3 install django mysqlclient
RUN mkdir /src
ADD django_web_app/ /src
