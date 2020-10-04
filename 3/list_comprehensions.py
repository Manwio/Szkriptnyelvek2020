#!/usr/bin/env python3

def main():
    #1.feladat
    l1 = ['auto', 'villamos', 'metro']
    l1_re = [s.upper() for s in l1]
    print(l1_re)

    #2.feladat
    l2 = ['aladar', 'bela', 'cecil']
    l2_re = [s.capitalize() for s in l2]
    print(l2_re)

    #3.feladat
    #l3 =[] NINCS
    l3_re = [0 for n in range(10)]
    print(l3_re)

    #4.feladat
    l4 = [n for n in range(1, 10+1)]
    l4_re = [n * 2 for n in l4]
    print(l4_re)

    #5.feladat
    l5 = [str(n) for n in range(1, 10+1)]
    l5_re = [int(s) for s in l5]
    print(l5_re)

    #6.feladat
    l6 = "1234567"
    l6_re = [int(s) for s in l6]
    print(l6_re)

    #7.feladat
    l7 = 'The quick brown fox jumps over the lazy dog'
    l7_re = [len(n) for n in l7.split()]
    print(l7_re)

    #8.feladat
    l8 = "python is an awesome language"
    l8_re = [n[0] for n in l8.split()]
    print(l8_re)

    #9.feladat
    l9 = 'The quick brown fox jumps over the lazy dog'
    l9_re = [(n, len(n)) for n in l9.split()]
    print(l9_re)

    #10.feladat
    #l10 = [] NINCS
    l10_re = [n for n in range(0, 10+1, 2)]
    print(l10_re)
    l10_re2 = [n for n in range(0, 10 + 1) if n % 2 == 0]
    print(l10_re2)

    #11.feladat
    l11 = [n for n in range(0, 20)]
    l11_re = [n * n for n in l11 if n * n % 2 == 0]
    print(l11_re)

    #12.feladat
    l12 = [n for n in range(0, 20)]
    l12_re = [n * n for n in l12 if str(n * n).endswith("4")]
    print(l12_re)

    #13.feladat
    #l13 = [] NINCS
    l13_re = "".join([chr(n) for n in range(ord('A'), ord('Z') + 1)])
    print(l13_re)

    #14.feladat
    l14 = [' apple ', ' banana ', ' kiwi']
    l14_re = [s.strip() for s in l14]
    print(l14_re)

    #15.feladat
    l15 = [1, 0, 1, 1, 0, 1, 0, 0]
    l15_re = "".join([str(n) for n in l15])
    print(l15_re)


if __name__ == "__main__":
    main()