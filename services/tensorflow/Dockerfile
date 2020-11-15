FROM tensorflow/tensorflow

RUN apt update && apt install -y xterm 

COPY open.sh /open.sh
RUN chmod +x /open.sh

COPY example_job.py /example_job.py

ENTRYPOINT [ "/comm_base/entrypoint.sh" ]