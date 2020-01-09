#!/usr/bin/env python3
##############################################################################
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################
'''This file realize the function of how to parser a config file.
This contain Two part:
Frist is Init some variables the will be used.
Second is reading config file.'''

import os
import yaml

class Parser():
    """配置文件解析"""
    gevjon_config = {}

    @classmethod
    def config_init(cls):
        cls.code_dir = os.path.dirname(os.path.abspath(__file__))
        cls.root_dir = os.path.dirname(cls.code_dir)
        config_dir = os.path.join(
            cls.root_dir,
            'config',
            'config.yaml')

        with open(config_dir) as file:
            config_info = yaml.safe_load(file)
            common_config = config_info['common_config']
            cls.gevjon_config['log_dir']= common_config['log_dir']
            cls.gevjon_config['apikey'] = common_config['apikey']
            cls.config_dir_check(cls.gevjon_config['log_dir'])

    @classmethod
    def config_dir_check(cls, dirname):
        if dirname is None:
            dirname = '/tmp/gevjon'
        if not os.path.exists(dirname):
            os.makedirs(dirname)

