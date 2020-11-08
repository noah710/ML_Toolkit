FROM node:latest

ENV PORT 8888
EXPOSE 8888

RUN apt update && apt install -y vim

COPY . /www
RUN chown -R node /www

USER node
WORKDIR /www
RUN npm install ws