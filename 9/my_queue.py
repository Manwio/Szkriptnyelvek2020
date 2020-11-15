#Írjunk egy MyQueue nevű osztályt, amely egy sor adatszerkezetet implementál két verem felhasználásával.
class Row:
    def __init__(self):
        self.queue_in = []
        self.queue_out = []

    #append: beszúrás a sor végére
    def append(self, number):
        self.queue_in.append(number)
        self.queue_out = self.queue_in[::-1]

        return self.queue_out

    #popleft: térjen vissza a sor első elemével (s ezt az elemet vegye is ki a sorból)
    def popleft(self):
        first_item = self.queue_out[0]
        self.queue_out = self.queue_out[1:]
        self.queue_in = self.queue_in[:-1]

        return first_item

    #is_empty: üres-e a sor
    def is_empty(self):
        if len(self.queue_out) == 0:
            return True
        else:
            return False

    #size: a sorban lévő elemek száma
    def size(self):
        return len(self.queue_out)


    def __str__(self):
        return "{w}".format(w=self.queue_out)


def main():
    r = Row()
    print(r.is_empty()) #True
    r.append(2)
    r.append(4)
    r.append(5)
    print(r) #[5, 4, 2]
    x = r.popleft()
    print(x) #5
    print(r) #[4, 2]
    print(r.is_empty()) #False
    print(r.size()) #2
    r.popleft()
    print(r)  # [2]
    r.popleft()
    print(r.is_empty()) #True
    print(r.size()) #0


main()