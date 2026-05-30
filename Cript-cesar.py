import socket
import time

SERVER_IP = '10.3.30.24'  # Substitua pelo IP do servidor
PORT = 5000


def cript_cesar(texto: str, chave: int) -> str:
    encriptado = []
    for char in texto:
        codigo = ord(char) + chave
        # mantem o resultado em caracteres ASCII imprimíveis
        if codigo > 126:
            codigo = 32 + ((codigo - 127) % (126 - 32 + 1))
        elif codigo < 32:
            codigo = 127 - ((32 - codigo) % (126 - 32 + 1))
        encriptado.append(chr(codigo))
    return ''.join(encriptado)


def main() -> None:
    texto_secreto = input('Texto secreto: ')
    while True:
        try:
            chave = int(input('Chave de deslocamento (inteiro): '))
            break
        except ValueError:
            print('Por favor, informe um número inteiro.')

    mensagem_encriptada = cript_cesar(texto_secreto, chave)
    print(f'Mensagem cifrada: {mensagem_encriptada}')

    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                client.connect((SERVER_IP, PORT))
                client.sendall(mensagem_encriptada.encode('utf-8'))
            print('Mensagem enviada ao servidor.')
        except Exception as error:
            print(f'Erro de conexão: {error}')

        time.sleep(1)


if __name__ == '__main__':
    main()
