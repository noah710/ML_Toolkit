FROM python:3.8-buster

RUN apt update && apt install -y spyder3

# run by listener to start spyder
COPY open.sh /open.sh
RUN chmod +x /open.sh
ENTRYPOINT [ "/comm_base/entrypoint.sh" ]