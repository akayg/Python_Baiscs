import socket as skt
server = skt.socket()
server.bind(('localhost', 8569))
server.listen(1)
# Accept the client and store both objects
client_socket, address = server.accept()
# Send message from server to client
client_socket.send("Hello from server".encode())
# Close both sockets
client_socket.close()
server.close()
