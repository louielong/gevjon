#!/usr/bin/env python3
# ^-^ coding=utf-8 ^-^

##############################################################################
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################

# > File Name: stock_index.py
# > Author: louie.long
# > Mail: longyu805@163.com
# > Created Time: Thu 26 Dec 2019 06:11:17 PM CST
# > Description:
# >

import tushare as ts

class stock_index():
  """通过Tushare获取股票相关数据"""

  def get_change_now(self, stock):
    df = ts.get_realtime_quotes(stock)
    return df

  def get_hist(self, stock, line):
    df = ts.get_hist_data(stock)
    data = df.head(line)
    return data