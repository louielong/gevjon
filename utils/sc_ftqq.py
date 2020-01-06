#!/usr/bin/env python3
# ^-^ coding=utf-8 ^-^

from requests import post

class sc_ftqq:
  """SeverChain message notification"""
  
  def __init__(self, apikey):
    self.api ="https://sc.ftqq.com/" + apikey + ".send"

  def set_data(self, title, content):
    ret = {
      "errno": 0,
      "errmsg": ''
    }
    if len(title) == 0:
      ret.errno = -1
      ret.errmsg = "Title cann't be empty."
      return ret
    elif len(title) >= 256:
      ret.errno = -1
      ret.errmsg = "Title is is longer than 256 char."
      return ret
    
    self.data = {
      
      "text": title,

      "desp": content
    }
    return ret

  def send_msg(self):
    req = post(self.api, data = self.data)
    return req
