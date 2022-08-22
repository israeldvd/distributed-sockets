import socket

HOST = '127.0.0.1'  # Interface local (localhost)
PORT = 1234  # Porta para troca de mensagem entre processos

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as skt:
    # Usa o objeto socket por meio do gerenciador de contexto
    print("Socket estabelecido")

    # Envia mensagem simples
    skt.sendto(input("Digite qualquer coisa:\n->"), (HOST, PORT))
