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

# Set local char
RUN echo "\nexport LC_ALL=C.UTF-8\nexport LANG=C.UTF-8\n" >> /root/.bashrc

#new required packages can be added here
RUN apt update && apt install -y \
    git \
    cron \
    python3 \
    python3-pip \
    python3-setuptools \
    --no-install-recommends

RUN git clone --depth=1 -b $BRANCH https://github.com/louielong/gevjon.git ${GEVJON_REPO_DIR}

RUN pip3 install --upgrade pip && \
    pip3 install setuptools --upgrade && \
    pip3 install -r ${GEVJON_REPO_DIR}/requirements/requirements.txt && \
    pip3 install -U ${GEVJON_REPO_DIR}
# link config file to python lib
RUN ln -fs ${GEVJON_REPO_DIR}/config/config.yaml /usr/local/lib/python3.6/dist-packages/config/config.yaml

# Set TimeZone, ubuntu 18.04 not have file /usr/share/zoneinfo/Asia/Shanghai
RUN cp -a /usr/local/lib/python3.6/dist-packages/pytz/zoneinfo/Asia/Shanghai \
    /etc/localtime && \
    export DEBIAN_FRONTEND=noninteractive && \
    apt install -y tzdata &&\
    apt -y autoremove && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

RUN cp -a ${GEVJON_REPO_DIR}/crontab/cron-file /etc/cron.d/cron-file && \
    chmod 0644 /etc/cron.d/cron-file && \
    crontab /etc/cron.d/cron-file && \
    touch /var/log/cron.log

ENV HOME $GEVJON_REPO_DIR
CMD ["sh", "-c", "/usr/sbin/cron && tail -f /var/log/cron.log"]
