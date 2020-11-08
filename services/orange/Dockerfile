FROM python:3.8-buster

RUN apt update && apt install -y libgl1 \
                                    libdbus-1-dev \
                                    libnss3 \
                                    libxcomposite1 \
                                    libxcursor1 \
                                    libxi6 \
                                    libxtst6 \
                                    libasound2 \
                                    virtualenv \
                                    build-essential \
                                    python3-dev \
                                    git \
                                    pyqt5-dev-tools

WORKDIR /
RUN pip install orange3

# listener starts this
COPY open.sh /open.sh
RUN chmod +x /open.sh

ENTRYPOINT [ "/comm_base/entrypoint.sh" ]