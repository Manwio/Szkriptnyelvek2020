#!/usr/bin/env python3

def draw(li):
    table_top = "+-----------------+"
    dot = "."
    queen = "Q"
    table_line2 = ""

    print(table_top)

    for n in li:
        for i in range(8):
            if n != i:
                table_line2 = table_line2 + dot + ' '
            else:
                table_line2 = table_line2 + queen + ' '

        print("|", table_line2, "|")
        table_line2 = ''

    print(table_top)

def main():
    draw([0, 4, 7, 5, 2, 6, 1, 3])

    print()

    draw([0, 1, 2, 3, 4, 5, 6, 7])

if __name__ == "__main__":
    main()