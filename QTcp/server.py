from socketserver import TCPServer, BaseRequestHandler
import time
class ServerHandler(BaseRequestHandler):
    def handle(self):
        print('Get connection from: ', self.client_address)
        while True:
            time.sleep(0.1)
            try:
                msg = self.request.recv(1024)
                msg = msg.decode('utf-8')
                print(msg)
                if msg == '':
                    print('Close connection: ', self.client_address)
                    break
                time.sleep(3)
                self.request.send(bytes(msg, 'utf-8'))

            except:
                print('Close connection: ', self.client_address)
                break

if __name__ == '__main__':
    print('+ + + Tester Serve Start ...')
    host = 'localhost'
    port = 23232
    server = TCPServer((host, port), ServerHandler)
    try:
        server.serve_forever()
    except:
        server.server_close()
