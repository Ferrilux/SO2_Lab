#! /bin/bash
# skrypt 1

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

# usuniecie wszystkich plikow z roszerzeniem .old
rm -f $1/*.old

# dodanie rozszerzenia .old
for FILE in `ls $1`
do
    # sprawdzenie czy obiekt jest plikiem i ma ustawione prawo do zapisu
    if [ \( -f "$1/$FILE" \) -a \( -w "$1/$FILE" \) ]
    then
        mv "$1/$FILE" "$1/${FILE}.old"
    fi
done