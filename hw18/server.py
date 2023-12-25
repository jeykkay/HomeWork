from socket import *

server = socket(
    AF_INET, SOCK_STREAM
)

server.bind(
    ('localhost', 7000)
)
server.listen(1)
user, addr = server.accept()
print(f'CONNECTED: {user}, {addr}')

while True:
    data = user.recv(1024)
    if not data:
        break
    user.send('You are connected'.encode('utf-8'))
user.close()
