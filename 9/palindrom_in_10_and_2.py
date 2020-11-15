#!/usr/bin/env python3

decimal = ''

def decimal_toBinary(num):
    return bin(num).replace('0b', '')

def is_palindrom_10_and_2(i):
    if i == int(str(i)[::-1]) and str(decimal_toBinary(i)) == str(decimal_toBinary(i))[::-1]:
        return True
    else:
        return False


def main():
    palindromsum_li = []

    for i in range(1000000):
        if is_palindrom_10_and_2(i):
            palindromsum_li.append(i)

    #print(palindromsum_li)
    print(sum(palindromsum_li))


if __name__ == "__main__":
    main()
