#!/usr/bin/env python3

def main():
    numbers = [4, 6, 3, 5, 9]
    sum_multip = 1

    for x in numbers:
        sum_multip *= x

    print(f"A lista elemeinek szorzata: {sum_multip}")

    print()

    numbers2 = []
    sum_multip = 1

    for x in numbers2:
        sum_multip *= x

    print(f"A lista elemeinek szorzata: {sum_multip}")

if __name__ == "__main__":
    main()