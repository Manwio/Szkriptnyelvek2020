#!/usr/bin/env python3

MELY = 'aáoóuú'
MAGAS = 'eéiíöőüű'

MELY_RE = 0
MAGAS_RE = 1
VEGYES_RE = 2
NOTHING_RE = 3

def high_deep(s):
    masssalhangzo = 0
    mely = 0
    magas = 0

    for i in range(len(s)):
        if s[i] in MAGAS:
            magas += 1
        if s[i] in MELY:
            mely += 1
        else:
            masssalhangzo += 1

    if masssalhangzo != 0 and mely != 0 and magas == 0:
        return MELY_RE
        masssalhangzo = 0
        mely = 0
        magas = 0

    if masssalhangzo != 0 and magas != 0 and mely == 0:
        return MAGAS_RE
        masssalhangzo = 0
        magas = 0
        mely = 0

    if masssalhangzo != 0 and mely != 0 and mely != 0:
        return VEGYES_RE
        mely = 0
        magas = 0
        masssalhangzo = 0
    
    else:
        return NOTHING_RE


def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "$đĐä", "mägä$$äg"]

    for s in words:
        if high_deep(s) == MELY_RE:
            print(f"{s} -> Mély")
        if high_deep(s) == MAGAS_RE:
            print(f"{s} -> Magas")
        if high_deep(s) == VEGYES_RE:
            print(f"{s} -> Vegyes")
        if high_deep(s) == NOTHING_RE:
            print(f"{s} -> Semmilyen")


if __name__ == "__main__":
    main()
