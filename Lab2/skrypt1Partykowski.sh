#!/bin/bash

# Lab 3 - skrypt 1, Mikolaj Partykowski
# Tresc zadania:
#   W zadanym katalogu przerobić wszystkie 
#   dowiązania twarde wskazujące na pliki 
#   regularne w tym katalogu – na dowiązania symboliczne 
#   (trzeba pozostawić jeden plik/dowiązanie, na który wskażą pozostałe).

# sprawdzenie czy podany zostal jeden katalog
if [ "$#" -ne 1 ]
then
    echo "Podaj nazwe katalogu!"
    exit 1
fi

# sprawdzenie czy istnieje podany katalog
if [ ! -d $1 ]
then 
    echo "Nie ma takiego katalogu!"
    exit 2
fi

directory=`ls -i | sort -n`

files=`ls  -i | sort -n`
index=1;
previous='init';
for file in $files
do
    if [ $((index%2)) -eq 0 ]
    then
        echo $file
        # robimy dowiazania do pierwszego pliku
        if [ $index -ge 2 ]
        then
            if [ $(realpath  ./$file) -ef $(realpath ./$previous) ]
            then
                ln -s $1/$file
                rm $1/$file
            fi
        fi
        previous=$file
    fi
    index=$[index+1]
done
exit