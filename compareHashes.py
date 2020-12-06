import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

hash1 = hashlib.new('ripemd160')
hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():
    print('{} e {} sao arquivos diferentes.\n{}: {}\n{}: {}'.format(arquivo1, arquivo2, arquivo1, hash1.hexdigest(), arquivo2, hash2.hexdigest()))
else:
    print('{} e {} sao arquivos iguais.\n{}: {}\n{}: {}'.format(arquivo1, arquivo2, arquivo1, hash1.hexdigest(), arquivo2, hash2.hexdigest()))