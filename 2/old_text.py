#!/usr/bin/env python3

TEXT = """Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
"""

def main():
    replace_items = (('a', 'c'), ('b', 'd'), ('c', 'e'), ('d', 'f'), ('e', 'g'),
                    ('f', 'h'), ('g', 'i'), ('h', 'j'), ('i', 'k'), ('j', 'l'),
                    ('k', 'm'), ('l', 'n'), ('m', 'o'), ('n', 'p'), ('o', 'q'),
                    ('p', 'r'), ('q', 's'), ('r', 't'), ('s', 'u'), ('t', 'v'),
                    ('u', 'w'), ('v', 'x'), ('w', 'y'), ('x', 'z'), ('y', 'a'), ('z', 'b'))

    abc = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

    newtext = TEXT.lower()

    newtext2 = []

    for w in newtext:
        if w in abc:
            for old, new in replace_items:
                if w == old:
                    newtext2.append(w.replace(old, new))

    print(newtext2)


if __name__ == "__main__":
    main()