import socket
import time

host = "localhost" # Replace by server IP address
server_port = 12800
local_port = 80

connection_to_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection_to_server.bind(('0.0.0.0', local_port))
connection_to_server.connect((host, server_port))
print("Connection established with server on server_port {}".format(server_port))

# Uncomment below line to enable tcp keepalive from server side
#connection_to_server.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 10000, 3000))

msg_to_send = b""
waitack = "0"
while msg_to_send != b"close":
    if waitack == "0": 
       msg_to_send = input("> ")
    # only a-Z character in order to avoid error msg
       msg_to_send = msg_to_send.encode()
    # Sending msg to server
       connection_to_server.send(msg_to_send)
       server_reply = connection_to_server.recv(1024)
       print(server_reply.decode())  
    else:
     server_reply = connection_to_server.recv(1024)
    if server_reply == b"Please Confirm":
       msg_to_send = b"Confirmed"
       # Uncomment below line to add latency on server side
       #time.sleep(10)  # Delay for reply in seconds (idle time)
       connection_to_server.send(msg_to_send)
       waitack = "1"
    else:
       print(server_reply.decode())
       waitack="0"

print("Closing connection")
connection_to_server.close()