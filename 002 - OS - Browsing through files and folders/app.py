#https://docs.python.org/3/library/functions.html#open
import os
from utils import formata_tamanho

caminho_procura = input('Digite um caminho:') #'/'
termo_procura = input('Digite um termo:')#'dumper'


if caminho_procura and termo_procura:
    #  lista os arquivos do caminho
    for raiz, diretorios, files in os.walk(caminho_procura):
        for file in files:
            if termo_procura in file:
                try:
                    caminho_completo = os.path.join(raiz, file)
                    nome_arquivo, ext_arquivo = os.path.splitext(caminho_completo)
                    tamanho = os.path.getsize(caminho_completo)
                    #  print(nome_arquivo, ext_arquivo, tamanho)

                    print('#################################')
                    print('Encontrei o arquivo:', file)
                    print('Caminho:', caminho_completo)
                    print('Nome:', nome_arquivo)
                    print('Extensão', ext_arquivo)
                    print('Tamanho', formata_tamanho(tamanho))

                except PermissionError as e:
                    print("Sem permissão neste arquivo.")
                except FileNotFoundError as e:
                    print("Arquivo não encontrado.")
                except Exception as e:
                    print("Erro Desconhecido")