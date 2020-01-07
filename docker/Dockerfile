##############################################################################
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################

FROM ubuntu:18.04
LABEL maintainer="Louie.Long <longyu805@163.com>"

# Docker hub
LABEL image=l0uie/gevjon

# CI docker image label
ARG BRANCH=master

# Gevjon repo
ENV GEVJON_REPO_DIR /root/gevjon

# Set local
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

#new required packages can be added here
RUN apt update && apt install -y \
    git \
    cron \
    python3 \
    python3-pip \
    python3-setuptools \
    --no-install-recommends && \
    cp -a \
    /usr/local/lib/python3.6/dist-packages/pytz/zoneinfo/Asia/Shanghai \
    /etc/localtime && \
    export DEBIAN_FRONTEND=noninteractive && \
    apt install -y tzdata &&\
    apt -y autoremove && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

# Set TimeZone, ubuntu 18.04 not have file /usr/share/zoneinfo/Asia/Shanghai
# RUN cp -a /usr/local/lib/python3.6/dist-packages/pytz/zoneinfo/Asia/Shanghai /etc/localtime

RUN git clone --depth=1 -b $BRANCH https://github.com/louielong/gevjon.git ${GEVJON_REPO_DIR}

#RUN pip3 install --upgrade pip3
RUN pip3 install setuptools --upgrade
RUN pip3 install -r ${GEVJON_REPO_DIR}/requirements/requirements.txt
RUN pip3 install -U ${GEVJON_REPO_DIR}

RUN cp -a ${GEVJON_REPO_DIR}/crontab/cron-file /etc/cron.d/cron-file
RUN chmod 0644 /etc/cron.d/cron-file
RUN crontab /etc/cron.d/cron-file
RUN service cron start

ENTRYPOINT [ "/bin/bash" ]