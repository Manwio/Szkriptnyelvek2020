#!/usr/bin/env python3

def isthis_palindrom_v1(s):
    news = s[::-1]
    if news == s:
        print("Palindrom")
    else:
        print("Nem palindróm")

def isthis_palindrom_v2(s):
    if s == s[::-1]:
        print("Palindrom")
    else:
        print("Nem palindróm")

def isthis_palindrom_v3(s):
    news = s[::-1]
    i = 0
    tof = True
    while i < len(s) and tof:
        if s[i] == news[i]:
            tof
            i += 1
        else:
            tof = False

    if tof == True:
        print("Palindrom")
    else:
        print("Nem palindrom")

def isthis_palindrom_v4(s):
    if len(s) < 2:
        return print("Palindróm")
    if s[0] != s[-1]:
        return print("Nem palindróm")
    else:
        return isthis_palindrom_v4(s[1:-1])


def main():
    word1 = 'seres'
    word2 = 'görög'
    word3 = "semmi"
    word4 = "kék"
    word5 = "alma"


    print("1.megoldás: (a)")

    isthis_palindrom_v1(word1)
    isthis_palindrom_v1(word2)
    isthis_palindrom_v1(word3)
    isthis_palindrom_v1(word4)
    isthis_palindrom_v1(word5)

    print()
    print("1.megoldás: (b)")

    isthis_palindrom_v2(word1)
    isthis_palindrom_v2(word2)
    isthis_palindrom_v2(word3)
    isthis_palindrom_v2(word4)
    isthis_palindrom_v2(word5)

    print()
    print("2.megoldás:")

    isthis_palindrom_v3(word1)
    isthis_palindrom_v3(word2)
    isthis_palindrom_v3(word3)
    isthis_palindrom_v3(word4)
    isthis_palindrom_v3(word5)

    print()
    print("3. megoldás:")

    isthis_palindrom_v4(word1)
    isthis_palindrom_v4(word2)
    isthis_palindrom_v4(word3)
    isthis_palindrom_v4(word4)
    isthis_palindrom_v4(word5)


if __name__ == '__main__':
    main()