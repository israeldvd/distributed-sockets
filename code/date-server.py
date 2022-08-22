import socket
from datetime import datetime

HOST = '127.0.0.1'  # Interface local (localhost)
PORT = 1234  # Porta para troca de mensagem entre processos

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as skt:
    print("Socket estabelecido")

    # Aloca um buffer para ouvir conexões
    skt.bind((HOST, PORT))

    # Retorna valores mensagem (bytes) e endereço do cliente
    msg, end_client = skt.recvfrom(1024)

    # Exibe esses retornos
    print("Mensagem do cliente:\n", msg)
    print("Endereço do cliente:\n", end_client)

    # Envia hora e data atual
    skt.sendto(bytes(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                     'utf8'), end_client)
