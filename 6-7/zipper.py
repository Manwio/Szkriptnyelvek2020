#!/usr/bin/env python3

def main():
    chars = "abcdefghijklmnopqrstuvwxyz"
    codes = [ord(s) for s in chars]

    result = list(zip(chars, codes))

    print(result)

    #for ca, co in result:
    #    print(ca, co)

if __name__ == "__main__":
    main()