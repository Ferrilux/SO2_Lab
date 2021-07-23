#!/usr/bin/env python3

# Mikołaj Partykowski 241145
# Zadanie 2: Skopiować zadane drzewo katalogów w zadane miejsce,
# uwzględniając pliki regularne, podkatalogi oraz dowiązania symboliczne.
# Dowiązania symboliczne w kopii powinny wskazywać na pierwotne obiekty.

import os
import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Niepoprawna ilosc argumentow!')
        sys.exit(1)

    source = sys.argv[1]
    destination = sys.argv[2]

    if not os.path.isdir(source):
        print(f'{source}: Podany plik nie istnieje lub nie jest katalogiem!')
        sys.exit(2)

    if not os.path.isdir(destination):
        print(f'{destination}: Podany plik nie istnieje lub nie jest katalogiem')
        sys.exit(3)

    for found, dirs, files in os.walk(source):
        for file in dirs + files:
            path = os.path.join(found, file)
            dest_file = os.path.join(
                destination, path[path.index(source) + len(source):])

            if os.path.islink(path):
                target = os.path.realpath(path)
                os.symlink(target, dest_file)

            elif os.path.isdir(path):
                os.mkdir(dest_file)

            elif os.path.isfile(path):
                os.mknod(dest_file)
