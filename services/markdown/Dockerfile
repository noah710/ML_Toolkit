FROM ubuntu:bionic

RUN apt update && apt install -y wget python3 dconf-gsettings-backend gir1.2-glib-2.0 gir1.2-gtk-3.0 gir1.2-gtksource-3.0 python3-markdown python3-bs4 gir1.2-webkit-3.0 yelp wkhtmltopdf python3-gi

WORKDIR /
RUN wget https://remarkableapp.github.io/files/remarkable_1.87_all.deb
RUN dpkg -i remarkable_1.87_all.deb

# listener starts this
COPY open.sh /open.sh
RUN chmod +x /open.sh

ENTRYPOINT [ "/comm_base/entrypoint.sh" ]