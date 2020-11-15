import random

def shuffle_v1(li):
    li_re = li.copy()
    random.shuffle(li_re)
    return li_re


def main():
    li = [1, 5, 7, 3, 2, 4]
    print('Alap:', li)

    li_s = shuffle_v1(li)
    print('Kevert lista:', li_s, "Utolsó:", li_s[-1])

    print('Alap', li)

main()