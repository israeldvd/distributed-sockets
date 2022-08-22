import socket

HOST = '127.0.0.1'  # Interface local (localhost)
PORT = 1234  # Porta para troca de mensagem entre processos

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM):
  pass # Usa o objeto socket por meio do gerenciador de contexto -- desfaz necessidade de close()