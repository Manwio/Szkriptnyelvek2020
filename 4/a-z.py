#!/usr/bin/env python3

import sys

def main():
    """A függvény vissza adja a ./a-z.py program futtatásra
        az abcdefghijklmnopqrstuvwxyz -t adja vissza
    ha pedig ./z-a.py-ként hívjuk meg a függvényt, akkor
        az zyxwvutsrqponmlkjihgfedcba -t adja vissza
    """

    out = "abcdefghijklmnopqrstuvwxyz"
    out2 = "zyxwvutsrqponmlkjihgfedcba"
    if sys.argv[0] == "./a-z.py":
        print(out)
    if sys.argv[0] == "./z-a.py":
        print(out2)
    

if __name__ == "__main__":
    main()   
