## Sockets and Client/Server Programming

You can use Python to communicate with remote processes using a client/server model. A server listens for connection requests from clients across the network or even from the same machine. Clients know how to connect to the server given an **IP address and port number**. Upon connection, the server reads the request sent by the client and responds appropriately. In this way, applications can be broken down into specific tasks that are accomplished in separate locations.

The data that is sent back and forth over a socket can be anything you like in text or binary. Normally, the client sends a request for information or processing to the server, which performs a task or sends data back. The SMTP the server we connected to in the previous lecture is an example of  client/server communication.

The IP and port number of the server are generally well-known and advertised so the client knows where to find the service. For example, here is an illustration of a browser connecting to a Web server at `domain.com` (whose IP address is obtained via DNS) and port 80:

<img src="http://contentdeliverance.com/cms-school/wp-content/uploads/2011/05/client-server-diagram-internet.png" width=400>

### An analogy

<img src=figures/call-center1.jpg width=150 align=right> You can think of client/server programming like a call center for a bank. Imagine there is only one lonely service employee in the call center.  When a customer calls, the service employee answers the phone with a network *handshake* "Bank X, may I help you?". The customer and service employee then communicate using a specific protocol (in this case, arbitrary English plus bank terminology). The customer asks for their checking account balance. The service employee looks it up and responds with the data to the customer. Once all transactions are completed, either party can disconnect, thus, closing the connection. A socket connection is just such a phone-like connection.

This model doesn't scale very well however. Imagine 10,000 people are calling the bank at the same time. Depending on how our phone system worked, all but one would get a busy signal. A better model is to put waiting customers on hold, which is typically how sockets work.  With only one service employee, we could not service very many requests. The solution is to add more service employees that can answer more simultaneous calls:

<img src=figures/call-center2.jpg width=200> 

One question comes up: How can multiple users can connect via the same "port and IP address" to multiple physical servers or processes?   By analogy: when a customer calls the main bank number, the operator (now an automated menu/choice system) routes/transfers the call to the appropriate department, such as fraud, web support, mortgages, etc. The main phone number then can go back to waiting for another call after handing off the connection.  

The server that answers at the main port number responds a new thread or process for each incoming request.

Another important detail: bank service employees do not waste time, running in place, when no calls are coming in. They "sleep" until a call comes in. Analogously, the server blocks waiting on a request at the port rather than sitting in a spin loop, "picking up the phone" to see if anybody is there--it waits for a "telephone ring."

### Creating a server program

**Exercise**. Pair up with someone in class for this exercise. You will both switch off being the server and the client. The following script creates a server that listens at port 8000. One student should run this program while the other uses `telnet` from the commandline to contact the server from a different laptop. You can put this code into `server.py`:

```python
import socket
import netifaces as ni

# Create a serve socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = ni.ifaddresses('en0')[ni.AF_INET][0]['addr']
print("server listening at "+ip+":8000")
# (on linux it might be `eth0` not `en0`)
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
```

Then start it up with and it will show you the IP address of your machine. For example:

```bash
$ python /tmp/server.py
server listening at 192.168.0.105:8000
```

If you get error `nodename nor servname provided, or not known` then see [this answer](https://apple.stackexchange.com/questions/253817/cannot-ping-my-local-machine) or previous [sockets](sockets.md) notes.

Instead of writing code to open a raw socket to the server (which is as complicated as the server code above), we can simply use the UNIX `telnet` program as our client, for the purposes of this exercise. (When we need to communicate with a remote server as a client, the target will always be a web server. In that case we get to use a much higher level library, `urllib2`, without worrying about these low-level details.)  To test this out yourself, do this from the commandline:

```bash
$ telnet YOUR-IP-ADDRESS 8000
Trying YOUR-IP-ADDRESS...
Connected to localhost.
Escape character is '^]'.
hello         <--- handshake hello message from server
hi back atcha <--- what I type
hi back atcha <--- echoed back from the server
Connection closed by foreign host.
```

Now, try to connect to the other student's laptop using their IP address and port 8000.
