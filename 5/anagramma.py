#!/usr/bin/env python3

def is_this_anagramma_v1(text1, text2):
    """A függvény kap két szót és összehasonlítja, hogy a két szóban azonos betűk vannak e db számilag.
    Ha igen, akkor igaz értéket ad vissza mivel akkor anagramma, ha pedig nem az a két szó, akkor hamis értéket ad visza."""

    tof = True

    d1 = {}
    d2 = {}

    for s in text1.lower():
        if s != ' ':
            d1[s] = d1.get(s, 0) + 1

    for s in text2.lower():
        if s != ' ':
            d2[s] = d2.get(s, 0) + 1

    if d1 == d2:
        return tof

    else:
        return not tof


def normalize(text):
    """A föggvény kap egy szöveget, majd vissza adja teljesen kisbetűsen és szóköz mentesen"""

    t_re = ''

    for i in range(len(text)):
        if text[i] != ' ':
            t_re = t_re + text[i].lower()

        else:
            t_re = t_re + ''

    return t_re

def is_this_anagramma_v2(text1, text2):
    """A függvény kap két szót és összehasonlítja, hogy a két szóban azonos betűk vannak e db számilag.
    Ha igen, akkor igaz értéket ad vissza mivel akkor anagramma, ha pedig nem az a két szó, akkor hamis értéket ad visza."""

    tof = True

    d1 = {}
    d2 = {}

    text1 = normalize(text1)
    text2 = normalize(text2)

    for s in text1:
        d1[s] = d1.get(s, 0) + 1

    for s in text2:
        d2[s] = d2.get(s, 0) + 1

    if d1 == d2:
        return tof

    else:
        return not tof


def main():
    print(is_this_anagramma_v1('listen', 'silent'))
    print(is_this_anagramma_v1('Clint Eastwood', 'Old west action'))

    print('----------')

    print(is_this_anagramma_v2('listen', 'silent'))
    print(is_this_anagramma_v2('Clint Eastwood', 'Old west action'))

    #print('-----------')
    #print(normalize('Clint Eastwood'))


###########################

if __name__ == '__main__':
    main()