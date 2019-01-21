from Config import config
from ZeroHello import ZeroHello
from observable import Observable


class ZNBot(ZeroHello):
    event = Observable()

    class Error(Exception):
        pass

    def __init__(self):
        super().__init__()

    def updateSiteInfo(self):
        def cb(obj):
            self.siteInfo = obj
            self.siteInfoUpdated()

        self.send("siteInfo", [], cb)

    def siteInfoUpdated(self):
        if not self.siteInfo["cert_user_id"]:
            raise self.Error("No certificate available")
        self.event.trigger("siteInfoUpdated")

    def on_open(self):
        self.send("certSet", ["zeroid.bit"])
        self.updateSiteInfo()
        self.event.trigger("webSocketOpen")


if __name__ == "__main__":
    zb = ZNBot()

