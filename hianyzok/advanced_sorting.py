def my_func3(m):
    return m[1]

def main():
    li = [[2, 6], [1, 3], [5, 4]]
    #[ [1, 3], [5, 4], [2, 6] ]

    print(sorted(li, key=my_func3))

if __name__ == '__main__':
    main()