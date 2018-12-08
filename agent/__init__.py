import zerorpc
from agent.config import CONNURL,UUID_PATH
from agent.commer import Commanager
from agent.message import Message
import threading
class Agent:
    def __init__(self):
        self.msg=Message(UUID_PATH)
        self.comm=Commanager(self.msg)
    def start(self):
        while not threading.Event().wait(3):
            try:
                self.comm.sendmsg()
            except Exception as e:
                self.comm.shutdown()
    def stop(self):
        pass