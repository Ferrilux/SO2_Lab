#!/usr/bin/env python3

# Mikołaj Partykowski 241145
# Zadanie 1: W zadanym pliku tekstowym (zawierającym kod języka C)
# należy znaleźć i wylistować na ekran wszystkie teksty komentarzy
# o postaci /*....*/ (mogą być wiloliniowe jak i może być wiele
# komentarzy w jednej linii.

import os
import sys
import re

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Zla liczba argumentow!')
        sys.exit(1)

    filepath = sys.argv[1]

    if not os.path.isfile(filepath):
        print('Podany argument nie jest plikiem lub nie istnieje!')
        sys.exit(2)

    with open(filepath) as file:
        for found in re.findall(r'\/\*((?:.|\n)*?)\*\/', file.read()):
            print(found)
