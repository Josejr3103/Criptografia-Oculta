def decript_cesar(texto: str, chave: int) -> str:
    decriptado = []
    for char in texto:
        codigo = ord(char) - chave
        # mantem o resultado em caracteres ASCII imprimíveis
        if codigo > 126:
            codigo = 32 + ((codigo - 127) % (126 - 32 + 1))
        elif codigo < 32:
            codigo = 127 - ((32 - codigo) % (126 - 32 + 1))
        decriptado.append(chr(codigo))
    return ''.join(decriptado)