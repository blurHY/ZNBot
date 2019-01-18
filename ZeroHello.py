import ZiteUtils
from time import sleep
import requests
from Config import config
from ZiteBase import ZiteBase


class ZeroHello(ZiteBase):  # Admin Site
    ZeroHelloAddr = "1HeLLo4uzjaLetFx6NH3PMwFP3qbRbTf3D"

    def __init__(self):
        try:
            self.ZeroHelloKey = ZiteUtils.getWrapperkey(self.ZeroHelloAddr)
        except:
            requests.get(
                "http://" + config.ZeroNetAddr, headers={"ACCEPT": "text/html"}
            )
            while True:
                try:
                    self.ZeroHelloKey = ZiteUtils.getWrapperkey(self.ZeroHelloAddr)
                except:
                    sleep(120)
        super().__init__(self.ZeroHelloAddr)

    def addSite(self, siteaddr):
        self.send("siteAdd", siteaddr, lambda: None)

