#!/usr/bin/env python3

TEXT = """Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
"""

def main():
    newtext = TEXT

    newtext2 = """"""

    for w in newtext:
        if w.isupper():
            if ord(w) > 88:
                newtext2 += chr((ord(w)) - 24)
            else:
                newtext2 += chr((ord(w)) + 2)
        elif w.islower():
            if ord(w) > 120:
                newtext2 += chr((ord(w)) - 24)
            else:
                newtext2 += chr((ord(w)) + 2)
        else:
            newtext2 += w

    print(newtext2)


if __name__ == "__main__":
    main()