# Program sortujący pliki w folderze - wersja 1

import os
import shutil

path = input("Podaj ścieżkę: ")   # zmienna path - podaj lokalizacje plików - string
files = os.listdir(path)       # zmienna files - jakie pliki są w podanej lokalizacji

for file in files:
    filename,extension = os.path.splitext(file)     # pętla
    extension = extension[1:]

    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file,path+'/'+extension+'/'+file)


# w miejscę podaj ściężkę, należy podać gdzie znajduje się folder, w którym nastąpić ma sortowanie plików
