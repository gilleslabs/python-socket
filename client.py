import socket

host = "localhost" # Replace by server IP address
port = 12800

connection_to_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection_to_server.connect((host, port))
print("Connection established with server on port {}".format(port))

# Uncomment below line to enable tcp keepalive from server side
#connection_to_server.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 10000, 3000))

msg_to_send = b""
while msg_to_send != b"close":
    msg_to_send = input("> ")
    # only a-Z character in order to avoid error msg
    msg_to_send = msg_to_send.encode()
    # Sending msg to server
    connection_to_server.send(msg_to_send)
    server_reply = connection_to_server.recv(1024)
    print(server_reply.decode()) #

print("Closing connection")
connection_to_server.close()