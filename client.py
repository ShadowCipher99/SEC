import socket
from cryptography.fernet import Fernet

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "localhost"
port = 3000
client_socket.connect((host, port))
key = client_socket.recv(1024)

while True:
    message = input("Enter the message: ")
    encrypt_message = Fernet(key).encrypt(message.encode())
    client_socket.send(encrypt_message)
    server_message = client_socket.recv(1024)
    decrypt_message = Fernet(key).decrypt(server_message)
    print("From server:", decrypt_message.decode())
    if not message:
        break

client_socket.close()
