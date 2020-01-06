#!/usr/bin/env python3
# ^-^ coding=utf-8 ^-^

##############################################################################
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################

# > File Name: gevjon_cli.py
# > Author: louie.long
# > Mail: longyu805@163.com
# > Created Time: Tue 31 Dec 2019 02:27:55 PM CST
# > Description:
# >

import os
import sys
import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version='0.1')
@click.pass_context 
def cli(ctx):
    """cli for gevjon project

       commands:
       gevjon stock <option>
    """
    pass


@cli.command('stock', help='Get stock index')
@click.option('-d', '--debug', is_flag=True,
              default=False, help='Debug mode')
@click.option('-n', '--notsend', is_flag=True,
              default=False, help='Not send notification')
def stock(debug, notsend):
  if debug:
    os.environ["DEBUG"] = "true"
  if notsend:
    os.environ["NOTSEND"] = "true"
  sys.path.append('../')
  from gevjon.stock import send_stock_index
  send_stock_index()

cli.add_command(stock)

if __name__ == '__main__':
    cli()
