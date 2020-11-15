class Verem:
    def __init__(self):
        self.v = []

    def __str__(self):
        return "{w}".format(w=str(self.v)[:-1])

    def ures(self):
        if len(self.v) == 0:
            return True
        else:
            return False

    def betesz(self, number):
        self.v.append(number)

    def meret(self):
        return len(self.v)

    def kivesz(self):
        for i in range(len(self.v)):
            x = self.v[-1]
            while x != None:
                x = self.v[-1]
                self.v = self.v[:-1]

                if x == None:
                    return None

                else:
                    return x


def main():
    v = Verem()  #üres verem létrehozása
    print(v)    #[
    print(v.ures()) #True
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)  # [1 4 5
    print(v.meret())  # 3
    print(v.ures())  # False
    x = v.kivesz()
    print(x)  # 5
    print(v)  # [1 4
    v.kivesz()
    v.kivesz()  # most már üres
    x = v.kivesz()
    print(x)  # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)

main()