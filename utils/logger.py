#!/usr/bin/env python3
##############################################################################
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################
# Logging levels:
#  Level     Numeric value
#  CRITICAL  50
#  ERROR     40
#  WARNING   30
#  INFO      20
#  DEBUG     10
#  NOTSET    0

import logging
import os

from utils.parser import Parser as conf_parser
conf_parser.config_init()

class Logger:
    def __init__(self, logger_name):

        # if user set --debug as a cli parameter
        # we will set this variable "Debug" to output debug info.
        DEBUG = os.getenv('DEBUG')

        self.logger = logging.getLogger(logger_name)
        self.logger.propagate = 0
        self.logger.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        log_formatter = ('%(asctime)s '
                         '%(filename)s:%(lineno)d '
                         '%(levelname)s %(message)s')

        formatter = logging.Formatter(log_formatter)

        ch.setFormatter(formatter)
        if DEBUG is not None and DEBUG.lower() == "true":
            ch.setLevel(logging.DEBUG)
        else:
            ch.setLevel(logging.INFO)
        self.logger.addHandler(ch)

        log_path = conf_parser.gevjon_config["log_dir"]
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        log_file = os.path.join(log_path, 'gevjon.log')
        hdlr = logging.FileHandler(log_file)

        hdlr.setFormatter(formatter)
        hdlr.setLevel(logging.DEBUG)
        self.logger.addHandler(hdlr)

    def getLogger(self):
        return self.logger
