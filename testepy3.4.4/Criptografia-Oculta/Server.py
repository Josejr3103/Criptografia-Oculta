import socket
from Decript import decript_cesar

SERVER_IP = '0.0.0.0' #Escuta em todas as interfaces de rede
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_IP, PORT))
server.listen(5)
print("Servidor aguardando conexões na porta {}...".format(PORT))

while True:
    client_socket, addr = server.accept()
    print("Conexão aceita de {}:{}".format(addr[0], addr[1]))
    data = client_socket.recv(1024).decode('utf-8')
    print("[!] Mensagem recebida(criptografada) : {}".format(data))
    
    # Tentar todas as chaves de 0 a 100
    print("\n[*] Tentando descriptografar com chaves de 0 a 100:")
    for chave in range(101):
        mensagem_descriptografada = decript_cesar(data, chave)
        # Verifica se a mensagem contém apenas letras a-z (válida)
        if mensagem_descriptografada.isalpha() or mensagem_descriptografada.isalpha():
            print('  Chave [{}]: {}'.format(chave, mensagem_descriptografada))
    
    print()
    client_socket.close()