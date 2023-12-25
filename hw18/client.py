import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(
    ('localhost', 7000)
)
client.send('Hello!'.encode('utf-8'))
data = client.recv(1024)
client.close()