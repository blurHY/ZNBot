import json
import re
import socket
import sys

import websocket
import threading

from Config import config


class ZeroWebSocketBase:
    def __init__(self, wrapper_key, address=config.ZeroNetAddr, secure=False):
        try:
            self.ws = websocket.WebSocketApp(
                "%s://%s/Websocket?wrapper_key=%s"
                % ("wss" if secure else "ws", address, wrapper_key),
                on_message=self.on_message,
                on_error=self.on_error,
                on_close=self.on_close,
            )
            self.ws.on_open = self.on_open
            self.next_id = 1
            self.waiting_cb = {}
            t = threading.Thread(target=self.ws.run_forever, name="ZeroWsThread")
            t.start()
        except socket.error:
            raise ZeroWebSocketBase.Error("Cannot open socket.")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.ws.close()

    def on_open(self):
        pass

    def on_message(self, message):
        response = json.loads(message)
        print("Message", response)
        if response["cmd"] == "response":
            if self.waiting_cb[response["to"]]:
                self.waiting_cb[response["to"]](response["result"])
            else:
                print("Ws callback not found: \n {}".format(response))
            self.next_id += 1
        elif response["cmd"] == "error":
            self.next_id += 1
            raise ZeroWebSocketBase.Error(
                *map(
                    lambda x: re.sub(r"<[^<]+?>", "", x),
                    response["params"].split("<br>"),
                )
            )
        else:
            print(response)

    def on_error(self, error):
        print(error)

    def on_close(self):
        pass

    def send(self, cmd, args=[], callback=None):
        self.waiting_cb[self.next_id] = callback
        data = dict(cmd=cmd, params=args, id=self.next_id)
        self.ws.send(json.dumps(data))

    class Error(Exception):
        pass


if __name__ == "__main__":
    import ZiteUtils

    ws = ZeroWebSocketBase(
        ZiteUtils.getWrapperkey("1HeLLo4uzjaLetFx6NH3PMwFP3qbRbTf3D")
    )

