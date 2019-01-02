from time import sleep

import requests

import ZiteUtils
from Config import *
from ZiteBase import ZiteBase


class ZeroHello(ZiteBase):  # Admin Site
    ZeroHelloAddr = "1HeLLo4uzjaLetFx6NH3PMwFP3qbRbTf3D"

    def __init__(self):
        try:
            ZeroHelloKey = ZiteUtils.getWrapperkey(
                ZeroHelloAddr)
        except:
            requests.get("http://"+ZeroNetAddr,
                         headers={"ACCEPT": "text/html"})
            while True:
                try:
                    ZeroHelloKey = ZiteUtils.getWrapperkey(
                        ZeroHelloAddr)
                except:
                    sleep(120)
        super().__init__(ZeroHelloAddr)
