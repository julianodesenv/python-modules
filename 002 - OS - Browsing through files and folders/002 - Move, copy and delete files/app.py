import os
import shutil

path_origin = r'C:\Users\Juliano\Downloads\teste'
path_new = r'C:\Users\Juliano\Downloads\Aaaa'

try:
    os.mkdir(path_new)
except FileExistsError as e:
    print(f"Pasta {path_new} já existe.")

for root, dirs, files in os.walk(path_origin):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(path_new, file)

        #  COPY FILES
        if '.py' in file:
            shutil.copy(old_file_path, new_file_path)
            print(f"Arquivo {file} copiado com sucesso!")

        #  REMOVE FILES
        if '.py' in file:
            os.remove(new_file_path)
            print(f"Arquivo {file} removido com sucesso!")

        #  MOVE FILES
        #shutil.move(old_file_path, new_file_path)
        #print(f"Arquivo {file} movido com sucesso!")