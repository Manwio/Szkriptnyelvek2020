#!/usr/bin/env python3

def main():
    kisbetu = 0
    nagybetu = 0
    ketszam = 0
    speckar = 0

    pasw = []

    speck = ',.:;'
    szamok = '0123456789'
    abc = 'abcdefghijklmnopqrstuvwxyz'
    ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    f = open('passwords.txt', 'r')

    for line in f:
        line = line.rsplit('\n')

        for s in line:
            if s in abc:
                kisbetu = kisbetu + 1
            if s in ABC:
                nagybetu = nagybetu + 1
            if s in szamok:
                ketszam = ketszam + 1
            if s in speck:
                speckar = speckar + 1

        if kisbetu != 0 and nagybetu != 0 and ketszam > 1 and speckar != 0:
            pasw.append(line)

            kisbetu = 0
            nagybetu = 0
            ketszam = 0
            speckar = 0

    print('A helyes jelaszavak száma:', len(pasw))

    f.close()

if __name__ == "__main__":
    main()
