#!/usr/bin/env python3

# Mikołaj Partykowski 241145
# Zadanie 1: W zadanym katalogu utwórz pliki regularne o nazwach 
# pokrywających się z kolejnymi liniami w zadanym pliku 
# (tworzyć również pliki ze spacjami w nazwie). Jeżeli plik o 
# takiej nazwie już istnieje, to zmień prawa dostępu do niego, 
# usuwając wszystkim prawo do zapisu. Jeżeli obiekt o takiej 
# nazwie istnieje, a nie jest plikiem regularnym, to wyświetl 
# ostrzeżenie i nie zmieniaj go.

import os 
import sys
import stat

if __name__ == '__main__':
    
    # bo sys.argv[0] - nazwa wykonywanego programu
    if len(sys.argv) != 3:
        print('Zla liczba argumentow!')
        sys.exit(1)

    dirpath = sys.argv[1]
    filepath = sys.argv[2]

    if not os.path.isdir(dirpath):
        print('Plik podany jako pierwszy argument nie istnieje, lub nie jest katalogiem.')
        sys.exit(2)

    if not os.path.isfile(filepath):
        print('Plik podany jako drugi argument nie istnieje, lub nie jest plikiem regularnym')
        sys.exit(3)

    with open(filepath) as files:
        for file in files:
            file = file.strip('\n')
            filepath = os.path.join(dirpath, file)

            if os.path.exists(filepath):
                if os.path.isfile(filepath) and not os.path.islink(filepath):
                    change = stat.S_IMODE(os.lstat(filepath).st_mode)
                    os.chmod(filepath, change % ~stat.S_IWUSR & ~stat.S_IWGRP & ~stat.S_IWOTH)
                else:
                    print('Plik juz istnieje i nie jest plikiem regularnym!')
            else:
                os.mknod(filepath)