from ZNBotBase import ZNBot
from json import loads
import Text
import os


class ZeroTalkBot(ZNBot):
    ZeroTalkAddr = "1TaLkFrMwvbNsooF4ioKAY9EuxTBTjipT"

    def __init__(self):
        self.event.on("siteInfoUpdated", self.updateUserDataPath)
        super().__init__()

    def updateUserDataPath(self):
        # Don't use path.join.It's a bug of zeronet
        self.userDataPath = "data/users/{0}".format(self.siteInfo["auth_address"])
        self.userContentJsonPath = self.userDataPath + "/content.json"
        self.userDataJsonPath = self.userDataPath + "/data.json"

    def getData(self, cb):
        def parseData(raw):
            if raw:
                cb(loads(raw))
            else:
                cb(
                    {
                        "next_topic_id": 1,
                        "topic": [],
                        "topic_vote": {},
                        "next_comment_id": 1,
                        "comment": {},
                        "comment_vote": {},
                    }
                )

        self.getFile(self.userDataJsonPath, parseData, self.ZeroTalkAddr)

    def publishData(self, path, obj):
        def cb(res):
            if not res == "ok":
                raise self.Error("Publish failed: {}".format(res))

        self.writePublish(path, Text.jsonEncode(obj), cb)

    def writePublish(self, inner_path, data, callback):
        def cb(res):
            if not res == "ok":
                raise self.Error("fileWrite error")
            self.send(
                "as", [self.ZeroTalkAddr, "sitePublish", [None, inner_path]], callback
            )

        self.writeFile(inner_path, data, cb, self.ZeroTalkAddr)


if __name__ == "__main__":
    ztb = ZeroTalkBot()

    @ztb.event.on("siteInfoUpdated")
    def func():
        def got(data):
            # Modify your data
            ztb.publishData(ztb.userDataJsonPath, data)

        ztb.getData(got)
