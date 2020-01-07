#!/usr/bin/env python3
##############################################################################
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################
'''This file realize the function of how to setup gevjon
to your environment. This use setuptools tool to setup'''

from setuptools import setup, find_packages


setup(
    name="gevjon",
    version="0.1",
    py_modules=['cli/gevjon_cli'],
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'utils': [
            '*.py'
        ],
        'config': [
            '*.yaml'
        ],
    },
    url="",
    install_requires=["click"],
    entry_points={
        'console_scripts': [
            'gevjon=cli.gevjon_cli:cli'
        ],
    },
)
