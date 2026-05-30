import socket
from Decript import decript_cesar

SERVER_IP = '0.0.0.0' #Escuta em todas as interfaces de rede
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_IP, PORT))
server.listen(5)
print(f"Servidor aguardando conexões na porta {PORT}...")

while True:
    client_socket, addr = server.accept()
    print(f"Conexão aceita de {addr[0]}:{addr[1]}")
    data = client_socket.recv(1024).decode('utf-8')
    print(f"[!] Mensagem recebida(criptografada) : {data}")
    
    # Tentar todas as chaves de 0 a 100 mostrando apenas as mensagens que tem texto e são minúsculas (possíveis mensagens legíveis)
    print("\n[*] Tentando descriptografar com chaves de 0 a 100:")
    for chave in range(101):
        mensagem_descriptografada = decript_cesar(data, chave)
        if mensagem_descriptografada.isalpha() and mensagem_descriptografada.islower():
            print(f"  Chave [{chave}]: {mensagem_descriptografada}")
    
    print()
    client_socket.close()