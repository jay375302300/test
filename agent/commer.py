import zerorpc
from .config import CONNURL
class Commanager:
    def __init__(self,msg):
        self.msg=msg
        self.client=zerorpc.Client()
    def sendmsg(self):
        self.client.connect(CONNURL)
        result=self.client.send(self.msg)
        return result


