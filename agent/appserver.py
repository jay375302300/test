import zerorpc
class ServerRPC:
    def __init__(self):
        self.clients={}
    def send(self,msg):
        self.clients[msg['payload']['id']] = msg['payload']
        print(msg)
        return 'hello{}'.format(msg)
s=zerorpc.Server(ServerRPC())
s.bind('tcp://127.0.0.1:9002')
s.run()
