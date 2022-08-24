import socket


def client():
    host = '127.0.0.1'
    port = 8000

    client_socket = socket.socket()
    client_socket.connect((host, port))
    message = input('--> ')
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()
    if data == '':
        raise KeyboardInterrupt
    print(f'received message: {data}')
    client_socket.close()


def server():
    host = '127.0.0.1'
    port = 9000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print(f'Connection from {address}')
    data = conn.recv(1024).decode()
    if data == 'end':
        raise KeyboardInterrupt
    print(f'received message: {data}')
    conn.send('OK'.encode())
    print(f'send message: OK')


if __name__ == '__main__':
    while True:
        try:
            client()
            server()
        except KeyboardInterrupt:
            break
