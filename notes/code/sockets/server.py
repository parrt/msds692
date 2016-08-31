import socket

# Create a serve socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
print "server listening at "+ip+":8000"
serversocket.bind((ip, 8000)) # wait at port 8000
# Start listening for connections from client
serversocket.listen(5) # 5 is number of clients that can queue up before failure

# Wait for connection
(clientsocket, address) = serversocket.accept()

# Send a welcome
clientsocket.send("hello\n")

# Get up to 1000 bytes
data = clientsocket.recv(1000)
print data

# Echo it back to client
clientsocket.send(data)

clientsocket.close()
