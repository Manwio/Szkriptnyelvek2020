import itertools

def multiply(l):
    result = 1
    for x in l:
        result = result * x
    return result

def main():
    sum_6 = 90
    multiply_6 = 996300

    numbers = [ i for i in range(1, 45 + 1) ]
    winner1 = []
    winner_end = []

    for i in itertools.combinations(numbers, r=6):
        if sum(i) == sum_6:
            winner1.append(i)

    for i in winner1:
        if multiply(i) == multiply_6:
            winner_end.append(i)

    print(winner_end)

main()