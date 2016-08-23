## Sockets and Client/Server Programming

You can use Python to communicate with remote processes using a client/server model. A server listens for connection requests from clients across the network or even from the same machine. Clients know how to connect to the server via an IP address and port number. Upon connection, the server reads the request sent by the client and responds appropriately. In this way, applications can be broken down into specific tasks that are accomplished in separate locations.

The data that is sent back and forth over a socket can be anything you like in text or binary. Normally, the client sends a request for information or processing to the server, which performs a task or sends data back.

The IP and port number of the server are generally well-known and advertised so the client knows where to find the service.

### An analogy

You can think of client/server programming like a pizza-delivery place.  As an employee at the pizza place, you wait by the phone (you are the "server").  Upon receiving a call from a client, you send a "hello" message.  The client responds by sending you an order.  You acknowledge and write down the order (performing the server's task).  You or they hang up (connection closes).  Typically the server will spawn a thread to actually handle the request as it can be complicated, like making the pizza.  The server should go back to answering the phone rather than using a single-threaded model and making the pizza itself.  Note: the server blocks waiting on a request at the port rather than sitting in a spin loop, "picking up the phone" to see if anybody is there--it waits for a "telephone ring."

### Creating a server program

```python
import socket

# Create a serve socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('127.0.0.1', 8000)) # wait at port 8000
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
```

### Creating a client program

For our purposes, we can simply use `telnet` as our client program. When we need to communicate with a remote server as a client, it will always be a web server. In that case we get to use a much higher level library, `urllib2`, without worrying about these low-level details. To make this work, start up the server from the previous section and then do this from the commandline:

```bash
$ telnet 127.0.0.1 8000
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
hello         <--- handshake hello message from server
hi back atcha <--- what I type
hi back atcha <--- echoed back from the server
Connection closed by foreign host.
```
