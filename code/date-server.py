import socket
from datetime import datetime

HOST = '127.0.0.1'  # Interface local (localhost)
PORT = 12345  # Porta para troca de mensagem entre processos
TIMEOUT = 20  # Definição de timeout para espera de conexão

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as skt:
    # Aloca um buffer para ouvir conexões
    skt.settimeout(TIMEOUT)  # Define um timeout em segundos
    try:
        skt.bind((HOST, PORT))
        print("Ligação do socket estabelecida")
    except:
        print('Erro: falha ao ligar socket ao endereço')
        exit()

    # Retorna valores mensagem (bytes) e endereço do cliente
    while True:
        try:
            msg, end_client = skt.recvfrom(1024)

            # Exibe esses retornos
            print("Mensagem do cliente:\n", msg)
            print("Endereço do cliente:\n", end_client, end="\n\n")

            # Envia hora e data atual
            skt.sendto(bytes(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                             'utf8'), end_client)

        except socket.timeout as e:
            # Abre exceção após tempo de esperada findado
            print(e, f': nenhuma conexão após {TIMEOUT} segundos...')
            break
