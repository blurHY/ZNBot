from ZeroWebsocketBase import ZeroWebSocketBase
from json import loads


class ZeroWs(ZeroWebSocketBase):

    def addZite(self, address):
        try:
            self.send("siteAdd", address)
        except self.Error as e:
            if e == "Invalid address":
                raise ZeroWsException("Site address invalid")

    def getZiteInfo(self, address):
        return self.send("as", address, "siteInfo")

    def getFile(self, file, target_site=None):
        if target_site:
            return self.send("as", target_site, "fileGet", file)
        else:
            return self.send("fileGet", file)

    def queryDb(self, address, query):
        return self.send("as", address, "dbQuery", query)


class ZeroWsException(Exception):
    pass
