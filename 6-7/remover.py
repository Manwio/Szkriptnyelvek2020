#!/usr/bin/env python3

INPUT = 'string1.py'
OUTPUT = 'string1_clean.py'

def main():
    with open(INPUT, 'r') as f, open(OUTPUT, 'w') as to:
        for line in f:

            if line.startswith('#'):
                line = line.rstrip('\n')
                to.write('')

            else:
                if '#' in line:
                    to.write('')

                else:
                    to.write(line)

    f.close()
    to.close()

if __name__ == "__main__":
    main()