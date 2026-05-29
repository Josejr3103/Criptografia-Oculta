import socket

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
    client_socket.close()