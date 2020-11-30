#!/usr/bin/env python3

def main():
    input_in = input('Adjon meg egy stringet: ')

    letters_dict = {}

    for s in input_in:
        if s not in letters_dict:
            letters_dict[s] = 1
        else:
            letters_dict[s] += 1

    for k in sorted(letters_dict):
        print(k * letters_dict[k])

if __name__ == "__main__":
    main()
