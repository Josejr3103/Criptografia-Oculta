# Criptografia Oculta

Projeto simples de criptografia/descriptografia usando cifra de César e comunicação via socket TCP.

O projeto possui três componentes:
- `Cript-cesar.py`: cliente que criptografa uma mensagem e envia ao servidor.
- `Server.py`: servidor que recebe a mensagem criptografada e tenta descriptografar usando chaves de 0 a 100.
- `Decript.py`: função de descriptografia importada pelo servidor.

## Tecnologias necessárias

- Python 3.x
- Biblioteca padrão do Python (`socket`, `os`, `time`)
- VirtualBox (para o caso de teste em VM)
- Windows 7 na VM no meu exemplo

## Instalação

1. Clone ou copie este repositório para uma pasta local.
2. Certifique-se de ter Python instalado.
3. O arquivo `.gitignore` já está configurado para excluir arquivos inúteis como `__pycache__/`, arquivos de ambiente e pastas de IDE.
4. Verifique o arquivo `.env` para definir o IP do servidor que o cliente deve usar.

### Configuração do `.env`

No arquivo `.env` desta pasta, deixe apenas:

```env
SERVER_IP=x.y.z.w
```

Altere `x.y.z.w` para o IP correto do servidor que estiver mandando a mensagem.

## Como usar

1. Abra um terminal na pasta do projeto.
2. Inicie o servidor:

```bash
python Server.py
```

3. Em outro terminal, execute o cliente:

```bash
python Cript-cesar.py
```

4. O cliente solicitará o texto secreto e a chave de deslocamento.
5. O servidor receberá a mensagem criptografada e tentará descriptografar com chaves de `0` a `100`.

## Teste em VM (caso de uso com VirtualBox e Windows 7)

### 1. Compartilhar pasta entre host e VM

- Na VM, vá em `Dispositivos` e ative `Inserir imagem de CD dos adicionais para convidado`.
- Em `Dispositivos > Pastas Compartilhadas > Configurações de pastas compartilhadas`:
  - Clique com o botão direito em cima das pastas existentes.
  - Escolha `Adicionar pasta compartilhada`.
  - Selecione o caminho da pasta `testepy3.4.4` no host.
  - Confirme.
- Se necessário, reinicie a VM.

### 2. Acessar pasta compartilhada na VM

- Abra o explorador de arquivos na VM.
- Na barra de endereço, digite:

```text
\\VBOXSVR\
```

- A pasta compartilhada deve aparecer.
- Copie o conteúdo para uma pasta de fácil acesso na VM, como `Downloads`.

### 3. Instalar Python 3.4.4 na VM

- Com o instalador `python-3.4.4.msi` do arquivo `testepy3.4.4`.
- Instale o Python.

### 4. Liberar porta 5000 no firewall

No prompt de comando como administrador, execute:

```cmd
netsh advfirewall firewall add rule name="Liberar Porta 5000" dir=in action=allow protocol=TCP localport=5000
```

Faça isso tanto na VM quanto no host, se quiser permitir o tráfego de rede entre eles.

### 5. Descobrir o IP da VM ou do host

No prompt de comando, execute:

```cmd
ipconfig | findstr IPv4
```

Use o IP exibido para atualizar a variável de ambiente `SERVER_IP` no `.env` ou para ajustar o código diretamente.

### 6. Rodar o projeto na VM

- Inicie o servidor no host ou na VM, dependendo de onde você quer que ele rode.
- Ajuste `SERVER_IP` no `.env` do cliente para o endereço do servidor.
- Execute `python Cript-cesar.py` e envie a mensagem.

## Observações

- O servidor já está configurado para tentar chaves de `0` a `100` e imprimir apenas resultados em letras minúsculas.
- Se você quiser mudar a porta, altere a constante `PORT` em `Cript-cesar.py` e `Server.py`.
- O arquivo `.env` deve permanecer apenas com a variável de IP do servidor.
