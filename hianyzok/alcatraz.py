def main():
    prisons = [0 for i in range(600 + 1)]
    free_prisons = []

    index = 1

    for i in range(1, 600 + 1):
        for j in range(1, 600 + 1):
            if j % index == 0:
                if prisons[j] == 0:
                    prisons[j] = 1
                else:
                    prisons[j] = 0
        index += 1

    for i in range(1, 600 + 1):
        if prisons[i] == 1:
            free_prisons.append(i)


    #print(prisons)
    print(free_prisons)

if __name__ == '__main__':
    main()