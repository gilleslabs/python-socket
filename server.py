import socket
import time

host = ''
port = 12800

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)
print("Server listening on {}".format(port))
# Uncomment below line to enable keepalive from server side
#server_socket.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 10000, 3000))
client_connection, connection_info = server_socket.accept()

client_data = b""
while client_data != b"close":
    client_data = client_connection.recv(1024)
    # On client side use only a-Z character in order to avoid error msg
    print(client_data.decode())
    time.sleep(10)  # Delay for reply in seconds (idle time)
    client_connection.send(b"Data received 5/5")

print("Closing connection")
client_connection.close()
server_socket.close()