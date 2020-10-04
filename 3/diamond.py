#!/usr/bin/env python3

def main():
    print("Adja meg milyen magas gyémántot szeretne: ")
    m = int(input())
    if m % 2 == 0:
        exit("HIBA!! Csak páratlan számot adhatsz meg!!")

    # Gyémánt közepe, legenerálása
    d = ['*' for db in range(m)]

    dia_middle = ""
    for middle in d:
        dia_middle += middle

    plusz_ter = m
    #Gyémánt teteje + kirajzolása
    for db in range(m):
        if db % 2 != 0:
            print(dia_middle[0:db].center(plusz_ter, ' '))

    # Gyémánt közepe + kirajzolás
    print(dia_middle.center(plusz_ter, ' '))

    #Gyémánt alja + kirajzolása
    for db in range(m):
        if db % 2 != 0:
            print(dia_middle[db:-1].center(plusz_ter, ' '))


if __name__ == "__main__":
    main()