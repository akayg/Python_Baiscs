import socket as skt

client = skt.socket()  # ✅ Creates a new socket object
client.connect(('localhost', 8569))  # ✅ Connects to server (must be running)

data = client.recv(1024).decode()  # ✅ Receives bytes and decodes to string
print("msg from server\n", data)   # ✅ Prints message

client.close()  # ✅ Closes connection
