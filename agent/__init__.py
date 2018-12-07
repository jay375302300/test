from agent.config import CONNURL
from agent.commer import Commanager
class Agent:
    def __init__(self,msg):
        self.msg=msg
        self.comm=Commanager(self.msg)

    def start(self):
        print(self.comm.sendmsg())
    def stop(self):
        pass