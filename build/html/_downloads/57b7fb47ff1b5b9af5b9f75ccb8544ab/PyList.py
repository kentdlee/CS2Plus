class PyList:
    # The size below is an initial number of locations for the list object. The
    # count instance variable keeps track of how many elements are currently stored
    # in the list since self.items may have empty locations at the end.
    def __init__(self,size=5):
        self.items = [None] * size
        self.count = 0

    def append(self,item):
        if self.count == len(self.items):
            # We must make the list bigger by allocating a new list and copying
            # all the elements over to the new list.
            newitems = [None] * self.count * 2
            for k in range(len(self.items)):
                newitems[k] = self.items[k]

            self.items = newitems
            
        self.items[self.count] = item
        self.count += 1

def main():
    p = PyList()

    for k in range(100):
        p.append(k)

    print(p.items)
    print(p.count)
    print(len(p.items))

if __name__ == "__main__":
    main()