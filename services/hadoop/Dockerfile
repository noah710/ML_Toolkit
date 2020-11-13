FROM sequenceiq/hadoop-docker:2.7.0

RUN ln -s /usr/local/hadoop-2.7.0 /hadoop-2.7.0
RUN ln -s /usr/local/hadoop /hadoop

RUN yum install -y xterm

COPY open.sh /open.sh
RUN chmod +x /open.sh

COPY example_job.sh /example_job.sh
RUN chmod +x /example_job.sh
 
COPY entrypoint.sh /special_entrypoint.sh
RUN chmod +x /special_entrypoint.sh

ENTRYPOINT [ "/special_entrypoint.sh" ]