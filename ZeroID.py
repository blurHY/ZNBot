from Config import config
import requests
from ZiteBase import ZiteBase
from json import loads


class ZerID(ZiteBase):
    ZeroIDAddr = "1iD5ZQJMNXu43w1qLB8sfdHVKppVMduGz"

    def __init__(self):
        super().__init__(self.ZeroIDAddr)

    def loaded(self):
        pass

    def on_open(self):
        self.loadUserJson()
        self.loaded()

    def loadUserJson(self):
        users = loads(self.getFile("data/users_archive.json"))["users"]
        users2 = loads(self.getFile("data/users.json"))["users"]
        for user, data in users2.items():
            users[str(user)] = data
        self.users = users

    def checkUserName(self, name):
        return bool(self.users.get(name))

    # Rules of zeroid
    # val = $(".username").val().toLowerCase()
    # val = val.replace /[^a-z0-9]/g, ""
    def register(self, user_name, auth_address=None, width=261):
        if self.checkUserName(user_name):
            raise self.Error("User name already taken")
        res = requests.post("https://zeroid.qc.to/ZeroID/request.php",
                            data={"auth_address": auth_address,
                                  "user_name": user_name, "width": width})
        if not res.ok:
            print("ZeroID register: {}".format(res.reason))
            raise self.Error(res)
        try:
            content = loads(res.text)
        except:
            raise self.Error(res)
        print("Solve task: {}".format(content["work_task"]))
        solution = eval(content["work_task"])  # TODO: Security check
        res = requests.post("https://zeroid.qc.to/ZeroID/solution.php", data={
                            "auth_address": auth_address,
                            "user_name": user_name,
                            "work_id": content["work_id"],
                            "work_solution": solution})
        if not res.ok:
            print("ZeroID register, submit solution: {}".format(res.reason))
            raise self.Error(res)

    class Error(Exception):
        pass


if __name__ == "__main__":
    zid = ZerID()
    ZerID.loaded = lambda: zid.register("horizonspider")
