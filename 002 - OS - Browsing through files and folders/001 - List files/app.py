#https://docs.python.org/3/library/functions.html#open
import os
from utils import formata_size

search_path = input('Digite um caminho:') #'/'
search_term = input('Digite um termo:')#'dumper'


if search_path and search_term:
    #  lista os arquivos do caminho
    for source, directories, files in os.walk(search_path):
        for file in files:
            if search_term in file:
                try:
                    full_path = os.path.join(source, file)
                    file_name, ext_file = os.path.splitext(full_path)
                    size = os.path.getsize(full_path)
                    #  print(file_name, ext_file, size)

                    print('#################################')
                    print('Encontrei o arquivo:', file)
                    print('Caminho:', full_path)
                    print('Nome:', file_name)
                    print('Extensão', ext_file)
                    print('size', formata_size(size))

                except PermissionError as e:
                    print("Sem permissão neste arquivo.")
                except FileNotFoundError as e:
                    print("Arquivo não encontrado.")
                except Exception as e:
                    print("Erro Desconhecido")