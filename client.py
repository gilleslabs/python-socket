import socket

host = "localhost"
port = 12800

connection_to_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection_to_server.connect((host, port))
print("Connection established with server on port {}".format(port))

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