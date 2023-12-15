import zipfile
import os

lab = ""
while lab.isnumeric() == False:
    lab = input("Escolha o número do laboratório: ")
lab = lab.zfill(2)

# Definindo as URLs de download e o diretório de trabalho
aux = f'https://susy.ic.unicamp.br:9999/mc102/{lab}/aux/aux{lab}.zip'
base = f'https://susy.ic.unicamp.br:9999/mc102/{lab}/aux/lab{lab}.py'
path_lab = f'Laboratório {lab}'

# Criando o diretório de trabalho
if not os.path.exists(path_lab):
    print(f'\nCriando o diretório "{path_lab}" ...')
    os.makedirs(path_lab)
else:
    print(f'\nO diretório "{path_lab}" já existe !!!')
    print("Ignorando a criação do diretório ...")
    
os.chdir(path_lab)

# Baixando o código base
if os.path.isfile(f"lab{lab}.py"):
    print(f'\nJá existe um arquivo lab{lab}.py no diretório "{path_lab}" !!!')
    print("Ignorando o download do código base ...")
else:
    print(f'\nBaixando o código base "lab{lab}.py" ...\n')
    os.system(f"curl -k -o lab{lab}.py {base} ")

    if os.path.isfile(f"lab{lab}.py"):
        print(f'Código base "lab{lab}.py" baixado com sucesso !!!')
    else:
        print(f'Não foi possível baixar o código base "lab{lab}.py" !!!')
        exit()

# Baixando os arquivos de teste
for teste in range(1,11):
    teste = str(teste).zfill(2)
    if os.path.isfile(f"arq{teste}.in") and os.path.isfile(f"arq{teste}.out"):
        teste_existe = True
    else:
        teste_existe = False
        break

if not teste_existe:
    print("\nOs arquivos de teste não foram encontrados !!!")
    print("Baixando os arquivos de teste ...\n")

    os.system(f"curl -k -o aux{lab}.zip {aux} ")
    with zipfile.ZipFile(f'aux{lab}.zip', 'r') as zip_ref:
        zip_ref.extractall()
    
    testes = os.listdir("./open")
    for arquivo in testes:
        source = os.path.join("./open", arquivo)
        destination = os.path.join("./", arquivo)
        os.rename(source, destination)
    os.remove(f'aux{lab}.zip')
    os.rmdir("open")
else:
    print("\nOs arquivos de teste já existem !!!")
    print("Ignorando o download dos arquivos de teste ...")



