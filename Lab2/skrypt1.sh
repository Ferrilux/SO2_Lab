#!/bin/bash

# Lab 3 (poprawiane) - Mikolaj Partykowski
# Tresc zadania:
#  W zadanym katalogu ($1) znaleźć dowiązania symboliczne do obiektów 
#  w tym samym katalogu $1 i usunąć je (dowiązania).

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

for file in $(ls -A $1)
do
    if [ -h $1/$file ] && [ $(dirname $(readlink -m $1/$file)) = $(realpath $1) ]
    then
        rm $1/$file
    fi 
done