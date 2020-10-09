#!/usr/bin/env python3

NUMBERS_1_TO_100 = [n for n in range(1, 100+1)]

def sum_1_to_100():
    """A függvény vissza adja 1-től 100-ig a számok összegét"""
    return sum(NUMBERS_1_TO_100)

def sum_1_to_100_v2():
    """A függvény vissza adja 1-től 100-ig a számok számjegyeinek összegét"""
    o_end = 0
    o_in = 0
    o_string = ''

    for n in NUMBERS_1_TO_100:
        o_string = str(n)

        for s in o_string:
            for i in range(len(s)):
                o_in = int(s[i])
                o_end += o_in

    return o_end


def main():
    print(f'1-től 100-ig a számok összege: {sum_1_to_100()}')
    print('----------')
    print(f'1-től 100-ig a számok számjegyeinek összege: {sum_1_to_100_v2()}')

if __name__ == '__main__':
    main()