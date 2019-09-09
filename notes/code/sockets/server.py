import socket
import netifaces as ni

# Create a serve socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = ni.ifaddresses('en0')[ni.AF_INET][0]['addr'] # might be en1 on mac
print("server listening at "+ip+":8000")
# (on linux it might be `eth0` not `en0`)
serversocket.bind((ip, 8000)) # wait at port 8000
# Start listening for connections from client
serversocket.listen(5) # 5 is number of clients that can queue up before failure

# Wait for connection
(clientsocket, address) = serversocket.accept()

# Send a welcome
clientsocket.send("hello from server\n".encode())

# Get up to 1000 bytes
data = clientsocket.recv(1000).decode()
print(data)

# Echo it back to client
clientsocket.send(data.encode())

clientsocket.close()
