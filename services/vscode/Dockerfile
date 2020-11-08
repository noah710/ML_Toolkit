FROM ubuntu:bionic

RUN apt update && apt install -y wget libnss3 gnupg apt libxkbfile1 libsecret-1-0 libgtk-3-0 libxss1 libgbm1 libx11-xcb-dev libxcb-dri3-0 libasound2 python3

WORKDIR /
RUN wget https://az764295.vo.msecnd.net/stable/fcac248b077b55bae4ba5bab613fd6e9156c2f0c/code_1.51.0-1604600753_amd64.deb
RUN dpkg -i code_1.51.0-1604600753_amd64.deb

# listener starts this
COPY open.sh /open.sh
RUN chmod +x /open.sh

ENTRYPOINT [ "/comm_base/entrypoint.sh" ]