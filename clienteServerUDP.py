import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Cliente socket criado com sucesso!')

host = 'localhost'
port = 5432
message = 'Ola servidor!'

try:
    print('Cliente: ' + message)
    s.sendto(message.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print('Cliente: ' + dados)
finally:
    print('\nCliente: Fechando a conexao.')
    s.close()