#!/usr/bin/env python3

def main():
    f1 = open('table1.txt', 'r')
    f2 = open('table2.txt', 'r')

    table1 = []
    table2 = []

    for line in f1:
        table1.append([int(i) for i in line.split()])

    for line in f2:
        table2.append([int(i) for i in line.split()])

    linesums_v1 = sum(max(line) - min(line) for line in table1)
    linesums_v2 = sum(max(line) - min(line) for line in table2)

    #print(table1)
    #print(table2)

    print(linesums_v1)
    print(linesums_v2)

    f1.close()
    f2.close()

if __name__ == "__main__":
    main()