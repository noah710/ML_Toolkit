ARG BASE_IMAGE=rstudio/r-base
FROM ${BASE_IMAGE}:bionic

ARG R_VERSION=4.0.3
ARG OS_IDENTIFIER=ubuntu-1804

# Install R
RUN wget https://cdn.rstudio.com/r/${OS_IDENTIFIER}/pkgs/r-${R_VERSION}_1_amd64.deb && \
    apt-get update -qq && \
    DEBIAN_FRONTEND=noninteractive apt-get install -f -y ./r-${R_VERSION}_1_amd64.deb && \
    ln -s /opt/R/${R_VERSION}/bin/R /usr/bin/R && \
    ln -s /opt/R/${R_VERSION}/bin/Rscript /usr/bin/Rscript && \
    ln -s /opt/R/${R_VERSION}/lib/R /usr/lib/R && \
    rm r-${R_VERSION}_1_amd64.deb && \
    rm -rf /var/lib/apt/lists/*

# install R studio
WORKDIR /
RUN apt update && apt install -y libgl1 libdbus-1-dev libnss3 libxcomposite1 libxcursor1 libxi6 libxtst6 libasound2
RUN wget https://download1.rstudio.org/desktop/bionic/amd64/rstudio-1.3.1093-amd64.deb && \
	apt install -y libedit2 libclang-dev libxkbcommon-x11-0 ; \
	apt --fix-broken install && \
	dpkg -i rstudio-1.3.1093-amd64.deb

# install python
RUN apt update && apt install python3 -y

# listener starts this
COPY open.sh /open.sh
RUN chmod +x /open.sh

RUN apt install python -y

ENTRYPOINT [ "/comm_base/entrypoint.sh" ]
