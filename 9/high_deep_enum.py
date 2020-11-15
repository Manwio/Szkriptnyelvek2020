#https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120910a

from enum import Enum

class Direction(Enum):
    MELY_MGHK = 'aáoóuú'
    MAGAS_MGHK = 'eéiíöőüű'
    MAGAS = 1
    MELY = 2
    VEGYES = 3
    SEMMILYEN = 4


def hangrend(s):
    mely = 0
    magas = 0
    masssalhangzo = 0

    for i in range(len(s)):
        if s[i] in Direction.MAGAS_MGHK.value:
            magas += 1
        if s[i] in Direction.MELY_MGHK.value:
            mely += 1
        else:
            masssalhangzo += 1

    if masssalhangzo != 0 and mely != 0 and magas == 0:
        masssalhangzo = 0
        mely = 0
        return Direction.MELY.value

    elif masssalhangzo != 0 and magas != 0 and mely == 0:
        masssalhangzo = 0
        magas = 0
        return Direction.MAGAS.value

    elif masssalhangzo != 0 and mely != 0 and mely != 0:
        mely = 0
        magas = 0
        masssalhangzo = 0
        return Direction.VEGYES.value

    else:
        return Direction.SEMMILYEN.value


def main():
    #print(Direction.MELY_MGHK) #Direction.UP
    #print(type(Direction.MELY_MGHK)) #<enum 'Direction'>
    #print(Direction.MELY_MGHK.name) #UP
    #print(Direction.MELY_MGHK.value) #1


    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "Pfffffff"]


    for s in words:
        w = hangrend(s)

        if w == Direction.MELY.value:
            print(f'{s} -> Mély')
        if w == Direction.MAGAS.value:
            print(f'{s} -> Magas')
        if w == Direction.VEGYES.value:
            print(f'{s} -> Vegyes')
        if w == Direction.SEMMILYEN.value:
            print(f'{s} -> Semmilyen')


main()