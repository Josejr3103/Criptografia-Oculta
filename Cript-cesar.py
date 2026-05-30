import os
import socket
import time


def load_env(path: str = '.env') -> None:
    if not os.path.isfile(path):
        return
    with open(path, 'r', encoding='utf-8') as env_file:
        for line in env_file:
            line = line.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip().strip('"\'"')
            if key and key not in os.environ:
                os.environ[key] = value


load_env()
SERVER_IP = os.getenv('SERVER_IP')
if not SERVER_IP:
    raise RuntimeError('SERVER_IP não definido. Edite o arquivo .env e defina SERVER_IP.')
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
