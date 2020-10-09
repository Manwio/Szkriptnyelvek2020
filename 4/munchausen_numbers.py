#!/usr/bin/env python3

def munchausen_number(number):
    """Egy természetes számot kapva, ellenőrzi,
    hogy a számjegyeket az épen adott számjegyet ugyan arra számjegy hatványrára emelve,
    majd ezen összegeket összeadva ugyan azt a természetes számot kapjuk vissza"""

    tof = True

    numbers = []
    for i in range(len(str(number))):
        numbers.append(int(str(number)[i]))

    m_numbers = []
    m_number = 0

    for i in range(len(numbers)):
        for n in numbers:
            if n == 0:
                m_number = 0
                m_numbers.append(m_number)

            else:
                m_number = n ** n
                m_numbers.append(m_number)

        if number == sum(m_numbers):
            return tof

        else:
            tof = False
            return tof


def main():
    numbers = [n for n in range(0, 10000 + 1)]

    munchausen_numbers = []

    for n in numbers:
        if munchausen_number(n):
            munchausen_numbers.append(n)

    print(munchausen_numbers)

    """
    numbers2 = [n for n in range(0, 440000000)]

    munchausen_numbers2 = []

    for n in numbers:
        if munchausen_number(n):
            munchausen_numbers2.append(n)

    print(munchausen_numbers2)
    # [0, 1, 3435, 438.579.088]
    """

if __name__ == '__main__':
    main()
