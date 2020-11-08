FROM python:3.8

RUN pip install jupyterlab

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A6DCF7707EBC211F && \
    apt update && apt install -y firefox-esr

COPY open.sh /open.sh
RUN chmod +x /open.sh

ENTRYPOINT [ "/comm_base/entrypoint.sh" ]