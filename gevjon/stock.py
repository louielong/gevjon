#!/usr/bin/env python3
##############################################################################
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################

import os
import json
import time

import utils.logger as log
from utils.stock_index import stock_index
from utils.sc_ftqq import sc_ftqq
from utils.parser import Parser as config

LOG = log.Logger(__name__).getLogger()

class Stock:
  """ Stock data process """
  def __init__(self):
    pass

  def get_sh_sz_index(self):
    index = stock_index()
    df = index.get_change_now(['sh','sz'])
    content = time.strftime('%Y-%m-%d %H:%M ',time.localtime(time.time()))
    if not df.empty:
      sh = df.iloc[0]
      sh_change = float(sh.price) - float(sh.pre_close)
      sh_ratio = (sh_change * 100)/float(sh.pre_close)
      sz = df.iloc[1]
      sz_change = float(sz.price) - float(sz.pre_close)
      sz_ratio = (sz_change * 100)/float(sz.pre_close)

      if sh_change > 0:
        content += "上证指数上涨: %.2f, 涨幅: %.2f%%, " % (sh_change, sh_ratio)
      elif sh_change < 0:
        content += "上证指数下跌: %.2f, 跌幅: %.2f%%, " % (sh_change, sh_ratio)
      elif sh_change == 0:
        content += "上证指数持平, "

      if sz_change > 0:
        content += "深证指数上涨: %.2f, 涨幅: %.2f%%。" % (sz_change, sz_ratio)
      elif sz_change < 0:
        content += "深证指数下跌: %.2f, 涨幅: %.2f%%。" % (sz_change, sz_ratio)
      elif sz_change == 0:
        content += "深证指数持平 。"
      LOG.info("%s" % content)
      return content
    else:
      LOG.error("Cann't get stock index.")
      return content

  def send_sh_sz_index_msg(self):
    content = self.get_sh_sz_index()
    if os.getenv('NOTSEND'):
      return
    if content:
      apikey = config.gevjon_config['apikey']
      if apikey != None:
        sc = sc_ftqq(apikey)
        LOG.debug("Bind SeverChain APIKEY %s" %apikey)
        ret = sc.set_data("上证、深证指数", content)
        if ret["errno"] == 0:
          LOG.debug("Set SeverChain message success.")
          req = sc.send_msg()
          if req.status_code != 200:
            LOG.error("Post request error, error code %d", req.status_code)
          elif req.status_code == 200:
            LOG.debug("Post request success")
            res = json.loads(req.text)
            if res["errno"] != 0:
              LOG.error("Send message failed %s", res["errmsg"])
            else:
              LOG.info("Send message success.")
        else:
          LOG.error("Set SeverChain message error. %s", ret["errmsg"])
          return
      else:
        LOG.error("Cann't get SeverChain APIKEY.")
        return
    else:
      LOG.error("Send sh and sz stock index failed.")

def send_stock_index():
  stock = Stock()
  stock.send_sh_sz_index_msg()


if __name__ == '__main__':
    send_stock_index()