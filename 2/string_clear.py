#!/usr/bin/env python3

def whitespace_clear(s):
    return ''.join(s.split(' '))

def main():
    text = "192.20.246.138:\n 6666"

    #1. értelmezés szerint
    print("".join(text.split()))

    print()

    #2. értelmezés szerint
    print(whitespace_clear(text))

if __name__ == "__main__":
    main()