import socket
from cryptography.fernet import Fernet

key = Fernet.generate_key()
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = ""
port = 3000
server_socket.bind((host, port))
server_socket.listen(2)
client_socket, client_addr = server_socket.accept()
client_socket.send(key)

while True:
    message = client_socket.recv(1024)
    decrypt_message = Fernet(key).decrypt(message)
    print("From client:", decrypt_message.decode())
    if not message:
        break
    server_message = input("Enter the message: ")
    encrypt_message = Fernet(key).encrypt(server_message.encode())
    client_socket.send(encrypt_message)

server_socket.close()
