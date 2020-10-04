#!/usr/bin/env python3

def main():
    l100_square_sum = sum([n * n for n in range(1, 100 + 1)])
    l100_sum_square = sum([n for n in range(1, 100 + 1)]) * sum([n for n in range(1, 100 + 1)])

    print(f"Az első 100 természetes szám négyzetösszege: {l100_square_sum}")
    print(f"Az első 100 természetes szám összegének a négyzete: {l100_sum_square}")

    print(f"Az első 100 természetes szám összegének a négyzete és az első 100 természetes szám négyzetösszege közti különbség: {l100_sum_square - l100_square_sum}")


if __name__ == "__main__":
    main()