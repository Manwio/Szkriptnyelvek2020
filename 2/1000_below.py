#!/usr/bin/env python3

def main():
    numbers = []

    for e in range(1, 1000):
        if e % 3 == 0:
            numbers.append(e)
        if e % 5 == 0:
            numbers.append(e)

    sum_numbers = 0

    for n in numbers:
        sum_numbers += n

    print(f"Összeg: {sum_numbers}")


if __name__ == "__main__":
    main()