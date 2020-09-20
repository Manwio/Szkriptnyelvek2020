#!/usr/bin/env python3

def main():
    print('A {0:d} | Hexadecimálisan: {0:x} | Binárisan: {0:b}'.format(21))

    print()

    book1 = ("Csillagok háborúja", "Margit néni")
    book2 = ("C baszás", "Gizi bácsi")
    book3 = ("Python kúrás", "Kedves űrlény")

    books = (book1, book2, book3)

    for x, y in books:
        print(f"The {x} was written by {y}")


if __name__ == '__main__':
    main()