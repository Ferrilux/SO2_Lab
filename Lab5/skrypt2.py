#!/usr/bin/env python3

# Autor: Mikołaj Partykowski 241145
# Zadanie 2: W zadanym katalogu przerób wszystkie 
# dowiązania symboliczne wskazujące na pliki regularne 
# (do których wykonujący skrypt nie ma prawa zapisu) 
# znajdujące się w tym katalogu, tak aby ścieżki dowiązania miały postać ./plik.

import os
import sys

if __name__ == '__main__':
    
    if len(sys.argv) != 2:
        print('Zla liczba argumentow!')
        sys.exit(1)

    dirpath = os.path.abspath(sys.argv[1])

    if not os.path.isdir(dirpath):
        print('Podany plik nie istnieje, lub nie jest katalogiem')
        sys.exit(2)

    for file in os.listdir(dirpath):
        filepath = os.path.join(dirpath, file)

        if os.path.islink(filepath):
            change = os.path.join(os.path.dirname(filepath), os.readlink(filepath))
            change = os.path.normpath(change)

            if os.path.isfile(change) and not os.access(change, os.W_OK) and os.path.dirname(change) == dirpath:
                os.remove(filepath)
                os.symlink('./' + os.path.basename(change), filepath)