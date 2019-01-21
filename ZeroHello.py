import ZiteUtils
from Config import config
from ZiteBase import ZiteBase


class ZeroHello(ZiteBase):  # Admin Site
    ZeroHelloAddr = "1HeLLo4uzjaLetFx6NH3PMwFP3qbRbTf3D"

    def __init__(self):
        super().__init__(self.ZeroHelloAddr)

    def addSite(self, siteaddr):
        self.send("siteAdd", siteaddr, lambda: None)

