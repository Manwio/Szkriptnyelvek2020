#!/usr/bin/env python3

def main():
    l1000 = [n for n in range(1, 1000) if n % 3 == 0 or n % 5 == 0]
    #print(l1000)
    print(sum(l1000))
    #233168

if __name__ == "__main__":
    main()