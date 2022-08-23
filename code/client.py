import socket

HOST = '127.0.0.1'  # Interface local (localhost)
PORT = 12345  # Porta para troca de mensagem entre processos
TIMEOUT = 10  # Espera alguns segundos antes de desistir

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as skt:
    # Usa o objeto socket por meio do gerenciador de contexto
    print("Socket estabelecido")

    # Envia mensagem simples
    skt.sendto(bytes(input("Digite qualquer coisa:\n->"), 'utf8'),
               (HOST, PORT))

    try:
        msg = skt.recv(1024)

        # Exibe esses retornos
        print("Mensagem do servidor:\n", msg.decode('utf8'), end="\n\n")

    except socket.timeout as e:
        print(e, f': nenhuma conexão após {TIMEOUT} segundos...')

    print("Finalização do socket")
