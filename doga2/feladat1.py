#!/usr/bin/env python3

import sys

def draw(s):
    lines = s.splitlines()
    maxlenline = 0

    for line in s.splitlines():
        if len(lines) > maxlenline:
            maxlenline = len(line)

    maxlenline += 3

    # Keret teteje
    print('+', end='')
    for i in range(maxlenline + 1):
        print('-', end='')
    print('+')

    #Keret közepe
    for lines in s.splitlines():
        print('|' + lines, end='')
        print((maxlenline - len(lines) + 1) * ' ', end='')
        print('|')


    # Keret alja
    print('+', end='')
    for i in range(maxlenline + 1):
        print('-', end='')
    print('+')

def main():
    if len(sys.argv) != 2:
        exit('Hiba: adjon meg egy szöveges file-t!')

    else:
        f = open(sys.argv[1], "r")
        draw(f.read())

        f.close()

if __name__ == "__main__":
    main()
