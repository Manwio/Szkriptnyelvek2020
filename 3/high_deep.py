#!/usr/bin/env python3

MELY = 'aáoóuú'
MAGAS = 'eéiíöőüű'


def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély"]

    masssalhangzo = 0
    mely = 0
    magas = 0

    for s in words:
        for i in range(len(s)):
            if s[i] in MAGAS:
                magas += 1
            if s[i] in MELY:
                mely += 1
            else:
                masssalhangzo += 1

        if masssalhangzo != 0 and mely != 0 and magas == 0:
            print(f"{s} -> Mély")
            masssalhangzo = 0
            mely = 0

        if masssalhangzo != 0 and magas != 0 and mely == 0:
            print(f"{s} -> Magas")
            masssalhangzo = 0
            magas = 0

        if masssalhangzo != 0 and mely != 0 and mely != 0:
            print(f"{s} -> Vegyes")
            mely = 0
            magas = 0
            masssalhangzo = 0


if __name__ == "__main__":
    main()