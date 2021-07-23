#!/bin/bash

# Laboratorium 4 - find
# Mikolaj Partykowski 241145

# Zadanie 2: Dla zadanych dwóch drzew katalogów utworzyć trzecie, 
# będące częścią wspólną dwóch pierwszych. 
# Aby utworzyć kopię, pliki/katalogi/dowiązania muszą się w obu tak 
# samo nazywać i mieć ten sam typ. Zawartość pliku regularnego lub ścieżka 
# dowiązania są nieistotne. W kopii zawsze jest to kopia z drzewa pierwszego.

# Argumenty : 1,2 - dwie nazwy katalogów, 3 - nazwa katalogu docelowego
if [ $# -ne 3 ]
then
    echo "Zla ilosc argumentow"
    exit 1
fi

if [ ! -d "$1" ]
then 
    echo "$1: Podany plik nie istnieje lub nie jest katalogiem"
    exit 1
fi

if [ ! -d "$2" ]
then 
    echo "$2: Podany plik nie istnieje lub nie jest katalogiem"
    exit 1
fi

mkdir -p "$3"

find "$1" -printf "%P\n" | while read -r file
do
    if [ -e "$2/$file" ]
    then
        if { [ -f "$1/$file" ] && [ -f "$2/$file" ]; } || { [ -h "$1/$file" ] && [ -h "$2/$file" ]; }
        then
            cp -P "$1/$file" "$3/$file"
        elif [ -d "$1/$file" ] && [ -d "$2/$file" ];
        then
            mkdir -p "$3/$file"
        fi
    fi
done