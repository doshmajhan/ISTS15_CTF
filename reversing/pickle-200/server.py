import pickle
import socketserver
import base64

class DontHackMeBro(socketserver.BaseRequestHandler):
    def handle(self):
        s = self.request
        data = s.recv(1024)
        out = pickle.loads(base64.b64decode(data))
        s.send("What am I supposed to do with {}".format(out))

def main():
    host = '0.0.0.0'
    port = 14623
    server = socketserver.ForkingTCPServer((host, port), DontHackMeBro)
    print("Running on {} port {}".format(host, port))
    server.serve_forever()

if __name__ == '__main__':
    main()

