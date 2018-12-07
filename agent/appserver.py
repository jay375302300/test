import zerorpc
class StraminRPC:
    def send(self,msg):
        print(msg)
        return 'hello{}',format(msg)
s=zerorpc.Server(StraminRPC())
s.bind('tcp://127.0.0.1:9000')
s.run()
