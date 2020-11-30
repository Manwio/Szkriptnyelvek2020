#!/usr/bin/env python3

def colltaz_make(number):
    re = [number]
    first = number

    while first != 1:
        if first % 2 == 0:
            first = first / 2
            re.append(first)

        else:
            first = 3 * first + 1
            re.append(first)

    return re

def colltaz_print(li):
    for i in li[:-1]:
        print(i, ' -> ', end='')
    print('1')

def main():
    c = colltaz_make(47)
    colltaz_print(c)
    print()
    print('A sorozat ', len(c), 'elemből áll.')


if __name__ == "__main__":
    main()
