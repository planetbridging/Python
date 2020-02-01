import socket, threading

class IncomingOutput(threading.Thread):
    def __init__(self,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        
    def PrintIncoming(self):
        data = ""
        while True:
            try:
                data = data +  self.csocket.recv(1024)
                print(data)
                return data.decode('utf-8')
            except:
                continue
                
    def run(self):
        while True:
            data = self.csocket.recv(2048)
            #in_data =  self.PrintIncoming()
            print(data.decode('utf-8'))


SERVER = input("Enter ip: ")
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
#client.sendall(bytes("This is from Client",'UTF-8'))
newthread = IncomingOutput(client)
newthread.start()

while True:
    command = input("Shell: ")
    client.sendall(bytes(command,'UTF-8'))
client.close()
