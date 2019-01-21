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

    def getFile(self, file, callback=None, target_site=None):
        if target_site:
            return self.send("as", [target_site, "fileGet", file], callback)
        else:
            return self.send("fileGet", [file], callback)

    def writeFile(self, file, data, callback=None, target_site=None):
        if target_site:
            return self.send("as", [target_site, "fileWrite", [file, data]], callback)
        else:
            return self.send("fileWrite", [file, data], callback)

    def queryDb(self, address, query, callback=None):
        self.send("as", [address, "dbQuery", query], callback)


class ZeroWsException(Exception):
    pass
