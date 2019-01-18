from os.path import join


class Config:
    def __init__(self):
        self._RootDir = ""
        self._sitesJson = ""

        self.RootDir = "/ZeroBundle/ZeroNet"
        self.DataDir = join(self.RootDir, "data")
        self.ZeroNetAddr = u"127.0.0.1:43110"

    @property
    def RootDir(self):
        return self._RootDir

    @RootDir.setter
    def RootDir(self, value):
        self._RootDir = value
        self.DataDir = join(value, "data")
        self._sitesJson = join(self.DataDir, "sites.json")

    @property
    def ContentDbPath(self):
        return join(self.DataDir, "content.db")

    @property
    def sitesJson(self):
        return self._sitesJson


config = Config()
