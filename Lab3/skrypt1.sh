#!/bin/bash

# Laboratorium 4 - find
# Mikolaj Partykowski 241145

# Zadanie 1: W zadanym drzewie katalogów znaleźć katalogi, 
# do których właściciel nie ma prawa odczytu, natomiast ktoś inny 
# (właściciel grupowy lub nie) ma prawo zapisu lub wykonania. 
# Skrypt nie powinien zakładać żadnych dodatkowych warunków dotyczących praw dostępu.

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

find "$1" -type d ! -perm -u=r -perm /go=wx -print