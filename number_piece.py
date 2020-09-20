#!/usr/bin/env python3

def main():
    number1=(2**256)
    number1_string=str(number1)

    print(len(number1_string))

    print('-------')

    number2=(123456789)
    number2_string=str(number2)

    print(len(number2_string))

if __name__ == '__main__':
    main()