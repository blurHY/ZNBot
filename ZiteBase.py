from ZeroWs import ZeroWs
from Config import *
import ZiteUtils


class ZiteBase(ZeroWs):
    def __init__(self, address):
        super().__init__(self.getWrapperKey(address))

    def getWrapperKey(self, address):
        return ZiteUtils.getWrapperkey(address)

    def isDownloaded(self, address=None):
        if address:
            return self.send("as", address, "siteInfo")["bad_files"] == 0
        return self.send("siteInfo")["bad_files"] == 0

    # Domain: zeroid.bit,kxoid.bit etc.
    def certSelect(self, address, cert_domain):
        return self.send("as", "certSet", cert_domain)


