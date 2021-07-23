#!/bin/bash

# Laboratorium 5 - grep, awk
# Mikolaj Partykowski 241145

# Zadanie: W zadanym drzewie katalogów wylistować nazwy wszystkich plików regularnych, 
# mających jedno z rozszerzeń o postaci „exe” (wielokrotne rozszerzenia to rozszerzenia, 
# od kropki do kropki lub do końca nazwy, gdy plik ma wiele kropek w nazwie).

if [ $# -ne 1 ]
then 
    echo "Niepoprawna ilosc argumentow"
    exit 1
fi

if [ ! -d "$1" ]
then
    echo "Podany plik nie jest katalogiem!"
    exit 1
fi

find $1 -type f -printf  "%f\n" | 
awk -F . ' 
BEGIN { FS = "/" } \ 
$NF ~ /[.]exe$|[.]exe[.].*$ / \
'