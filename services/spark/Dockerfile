FROM bitnami/spark:3-debian-10

USER root
RUN apt update && apt install -y xterm python

COPY open.sh /open.sh
RUN chmod +x /open.sh

COPY example_job.sh /opt/bitnami/spark/example_job.sh
RUN chmod +x /opt/bitnami/spark/example_job.sh

# modify existing entrypoint to start the listen server, kinda dirty :/
RUN bash -c "sed -i 's,exec "$@",python /comm_base/listener.py \&\nexec "$@",g' /opt/bitnami/scripts/spark/entrypoint.sh"

#ENTRYPOINT [ "/comm_base/entrypoint.sh" ]