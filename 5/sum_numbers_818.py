#!/usr/bin/env python3

def sum_numbers_818(n):
    """A függvény kap egy számot és visszaadja a számjegyeinek összegét"""
    sum_re = 0
    n_s = str(n)

    for s in n_s:
        sum_re += int(s)

    return sum_re

def main():
    print('Teszt: 2^15')
    n_t = 2**15
    print(sum_numbers_818(n_t))
    #26

    print('-----------')

    print('2^1000:')
    n = 2**1000
    print(sum_numbers_818(n))
    #1366

###########################

if __name__ == '__main__':
    main()