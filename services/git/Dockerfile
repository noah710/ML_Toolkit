FROM ubuntu:xenial

WORKDIR /

RUN apt update && apt install -y wget \
                                libgtk-3-0 \
                                libudev1 \
                                libgcrypt20 \
                                libnotify4 \
                                libxtst6 \
                                libnss3 \
                                libxkbfile1 \
                                libglib2.0-bin \
                                xdg-utils \
                                libxss1 \
                                libasound2 \
                                git \
                                python3

RUN wget https://release.gitkraken.com/linux/gitkraken-amd64.deb && \
    dpkg -i gitkraken-amd64.deb

COPY open.sh /open.sh
RUN chmod +x /open.sh

# install a browser to login to github with
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A6DCF7707EBC211F && \
    apt update && apt install -y firefox

RUN apt install python -y

ENTRYPOINT [ "/comm_base/entrypoint.sh" ]