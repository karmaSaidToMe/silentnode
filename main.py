import socket as sock

socket = sock.socket()
host   = sock.gethostname()
ip     = sock.gethostbyname(host)
port   = 8080

socket.bind(
    (
        host, 
        port
    )
)
print("Suc: socket.bind()")
print("Your IP", str(ip))

username = input('Enter username >>> ')
socket.listen(1)

connection, add = socket.accept()
print('Suc: connected from ', add[0])

client = (connection.recv(1024)).decode()
print(client + ' connected.')
connection.send(username.encode())

while True:
    msg = input('> ')
    connection.send(msg.encode())
    msg = connection.recv(1024)
    msg = msg.decode()
    print(client, ': ', msg)