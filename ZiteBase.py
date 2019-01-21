from ZeroWs import ZeroWs
from Config import *
import requests
from time import sleep
import ZiteUtils


class ZiteBase(ZeroWs):
    def __init__(self, addr):
        self.addr = addr
        try:
            self.wrappperKey = ZiteUtils.getWrapperkey(addr)
        except:
            requests.get(
                "http://" + config.ZeroNetAddr, headers={"ACCEPT": "text/html"}
            )
            while True:
                try:
                    self.wrappperKey = ZiteUtils.getWrapperkey(addr)
                except:
                    sleep(120)
        super().__init__(self.wrappperKey)

    def getWrapperKey(self, address):
        return ZiteUtils.getWrapperkey(address)

    def isDownloaded(self, address=None):
        if address:
            return self.send("as", address, "siteInfo")["bad_files"] == 0
        return self.send("siteInfo")["bad_files"] == 0

    # Domain: zeroid.bit,kxoid.bit etc.
    def certSelect(self, address, cert_domain):
        return self.send("as", "certSet", cert_domain)

