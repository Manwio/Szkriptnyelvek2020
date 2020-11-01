#!/usr/bin/env python3

INPUT = 'passphrase2.txt'

def main():
    counter = 0

    with open(INPUT, 'r') as f:
        for line in f:
             passphrase = line.rstrip('\n').split()

             if len(passphrase) == len(set(passphrase)):
                 counter += 1

             #print(passphrase)
             #print(set(passphrase))
             #print(len(passphrase))
             #print(len(set(passphrase)))

    print(counter)

    f.close()

if __name__ == "__main__":
    main()