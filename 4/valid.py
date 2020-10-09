#!/usr/bin/env python3

def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    """A függvény egy olyan (akár üres) sztringgel tér vissza, ami a "text"-ből (első paraméter)
    csak azokat a karaktereket adja vissza, melyek szerepelnek a "chars"-ban."""

    out_string = ""

    out_string += text[0]

    if chars:
        out_string = ""
        for s in text:
            if s in chars:
                out_string += s

    print(out_string)


def main():
    valid("Barking!")
    valid("KL754", "0123456789")
    valid("BEAN", "abcdefghijklmnopqrstuvwxyz")

if __name__ == '__main__':
    main()