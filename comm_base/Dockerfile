FROM python:3.8-buster

COPY listener.py /listener.py
COPY placeholder_open.sh /open.sh
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
