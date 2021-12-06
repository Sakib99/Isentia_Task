FROM ubuntu:20.04

MAINTAINER Sakib  Alam

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y python3 pip mysql-server vim mc wget curl less && apt-get clean
RUN pip install mysql-connector-python

EXPOSE 80

ENV FOLDER_PROJECT /var/sakib_mysql

RUN mkdir -p $FOLDER_PROJECT

COPY docker_run_mysql.sh $FOLDER_PROJECT
COPY start.sql $FOLDER_PROJECT
COPY src $FOLDER_PROJECT

RUN chmod +x /var/sakib_mysql/docker_run_mysql.sh

CMD ["/var/sakib_mysql/docker_run_mysql.sh"]
