#!/usr/bin/env python3

open_list = ["[","{","("]
close_list = ["]","}",")"]

def test(math_string):
    stack = []
    for i in math_string:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


def main():
    print(test("((5+3)*2+1)"))
    print(test("{[(3+1)+2]+}"))
    print(test("(3+{1-1)}"))
    print(test("[1+1]+(2*2)-{3/3}"))
    print(test("(({[(((1)-2)+3)-3]/3}-3)"))


if __name__ == "__main__":
    main()
