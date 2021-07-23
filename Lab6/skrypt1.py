#!/usr/bin/env python3

# Mikołaj Partykowski 241145
# Zadanie 1: W zadanym drzewie katalogów znaleźć
# katalogi zawierające co najmniej $2 podkatalogi
# inne niż ‘.’ i ‘..’.

import os
import sys

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print('Zla liczba argumentow!')
        sys.exit(1)

    dirpath = sys.argv[1]
    min_subs = int(sys.argv[2])

    if not os.path.isdir(dirpath):
        print(f'{dirpath}: Podany plik nie istnieje, lub nie jest katalogiem!')
        sys.exit(2)

    for found, *_ in os.walk(dirpath):
        found_subs = os.stat(found).st_nlink - 2
        if found_subs >= min_subs:
            print(found)
