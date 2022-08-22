import socket

HOST = '127.0.0.1'  # Interface local (localhost)
PORT = 1234  # Porta para troca de mensagem entre processos

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as skt:
    skt.bind((HOST, PORT))  # Aloca um buffer para ouvir conexões
    msg, end_client = skt.recvfrom(1024)

    print(msg, end_client)
