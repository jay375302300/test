import zerorpc
from agent.config import CONNURL
from agent.message import Message
import threading
class Commanager:
    def __init__(self,msg:Message,timeout=3):
        self.msg=msg
        self.client=zerorpc.Client()
        self.event=threading.Event()
        self.timeout=timeout
    def sendmsg(self):
        try:
            self.event.clear()
            self.client.connect(CONNURL)
            self.client.send(self.msg.reg())
            while not self.event.wait(self.timeout):
                self.client.send(self.msg.heart_beat())
        except Exception as e:
            raise e
    def shutdown(self):
        self.event.set()
        self.client.close()


