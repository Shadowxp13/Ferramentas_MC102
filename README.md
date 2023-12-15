# Descrição
Alguns scripts em Python que eu criei ou modifiquei para facilitar o download e teste automático das atividades da disciplina de "Algoritmos de Programação de Computadores" da Universidade Estadual de Campinas.

Junto com toda atividade disponibilizada no SuSy, são disponibilizados 20 arquivos de teste, dos quais 10 são arquivos ```arqXX.in```, os quais contêm as entradas do teste e os outros 10 são arquivos ```arqXX.out```, que contêm as saídas esperadas da sua atividade para essas entradas.

O Instituto de Computação disponibiliza um script para o teste das atividades, mas esse só funciona no ambiente Linux (presume-se que o aluno utilizará o Google Cloud Shell). Assim, realizei algumas modificações no código original (disponibilizado [aqui](https://ic.unicamp.br/~mc102/aulas/testador.py)) para que esse pudesse ser utilizado também no Windows.

# Dependências
```Python 3.x``` e ```curl```

# Uso
Primeiramente, deve-se baixar os scripts ```lab_downloader.py``` e ```testador.py``` no mesmo diretório.
## Baixando o código base e os testes das atividades
Para tal, deve-se executar o script ```lab_downloader.py```. Em seguida, o script solicitará o número da atividade, no formato de um ou dois dígitos (por exemplo, ```01```, ```1``` ou ```15```)

Assim, o script fará o download dos arquivos com a seguinte estrutura:

```
└── Laboratório XX
    ├── arq01.in
    ├── arq01.out
    ├── arq02.in
    ├── arq02.out
    ├── arq03.in
    ├── arq03.out
    ├── arq04.in
    ├── arq04.out
    ├── arq05.in
    ├── arq05.out
    ├── arq06.in
    ├── arq06.out
    ├── arq07.in
    ├── arq07.out
    ├── arq08.in
    ├── arq08.out
    ├── arq09.in
    ├── arq09.out
    ├── arq10.in
    ├── arq10.out
    └── labXX.py
```
É importante destacar que o script não sobrescreverá nenhum arquivo, evitando assim que ocorra alguma perda de código.

## Executando o testador
O testador respeita a mesma estrutura de arquivos que o downloader.
Logo, deve-se executar o script ```testador.pý```. Em seguida, o script solicitará o número da atividade, no mesmo formato que o script ```lab_downloader.py```. Em seguida, o usuário deve digitar ```1``` ou ```2```, de acordo com o que deseja realizar.

# Problemas conhecidos
Por algum motivo, no Windows, os caracteres acentuados não são preservados quando o código salva a output do arquivo ```labXX.py```. Assim. quando ocorre a comparação com os arquivos ```arqXX.out```, o testador reportará que o resultado está incorreto. Isso não ocorre quando o testador é executado no Linux.
