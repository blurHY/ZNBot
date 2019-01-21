from base64 import b64encode
from json import dumps


def jsonEncode(obj):
    return b64encode(dumps(obj, ensure_ascii=False).encode("UTF-8")).decode("UTF-8")


if __name__ == "__main__":
    print(jsonEncode({"hello": "Zerasdf士大'asdasd'asdasd`夫oNet"}))
