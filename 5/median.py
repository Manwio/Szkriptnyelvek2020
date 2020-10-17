#!/usr/bin/env python3
import statistics
import math

def median_v1(l):
    """A függvény kap egy számokkal teli listát majd vissza adja a mediánját a listának"""

    l_median = sorted(l)
    median_re = 0

    if len(l_median) % 2 == 0:
        median_re = (l_median[(len(l_median)//2) + 0] + l_median[(len(l_median)//2) - 1]) / 2

    else:
        median_re = l_median[(len(l_median)//2) + 0]

    return l_median, median_re

def main():
    l1 = [1, 2, 3, 4, 5]
    print(median_v1(l1))

    print(median_v1([3, 1, 2, 5, 3]))
    print(median_v1([1, 300, 2, 200, 1]))
    print(median_v1([3, 6, 20, 99, 10, 15]))

###########################

if __name__ == '__main__':
    main()