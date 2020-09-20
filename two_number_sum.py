#!/usr/bin/env python3
import sys

def two_number_sum_v1():
    numbers_sum = int(sys.argv[1]) + int(sys.argv[2])
    print(numbers_sum)


def main():
    two_number_sum_v1()


if __name__ == '__main__':
    main()