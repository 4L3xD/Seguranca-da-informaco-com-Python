import hashlib

string = input('Digite o texto a ser gerada a hash: ')
menu = int(input('''### ESCOLHA O TIPO DE HASH ###
                1) MD5
                2) SHA1
                3) SHA256
                4) SHA512
                Digite p número do hash a ser gerado: '''))
if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print('Hash MD5 da string: ', resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print('Hash SHA1 da string: ', resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print('Hash SHA256 da string: ', resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print('Hash SHA512 da string: ', resultado.hexdigest())
else:
    print('Algo de errado não deu certo!')


