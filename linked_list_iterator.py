class LinkedList:
    def __init__(self, collection=None):
        self.head = None
        if collection:
            for item in reversed(collection):
                self.insert(item)

    def __iter__(self):
        def value_generator():
            current = self.head
            while current:
                yield current.value 
                current = current.next 
        return value_generator()

    def __str__(self):
        out = ''
        for value in self:
            out += f'[{value}] -> '
        out += 'None'
        return out 

    def __reversed__(self):
        return list(self)[::-1]

    def __len__(self):
        return len(list(iter(self)))

    def __eq__(self, other):
        return list(self) == list(other) 

    def __lt__(self, other):
        return list(self) < list(other)

    def __getitem__(self, index):
        for i, item in enumerate(self):
            if i == index:
                return item
        raise IndexError 

    def insert(self, value):
        self.head = Node(value, self.head)

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        
        current = self.head

        while current.next:
            current = current.next

        current.next = node

class Node:
    def __init__(self, value, next_ = None):
        self.value = value
        self.next = next_

if __name__ == "__main__":
    def gen():
        for i in range(10):
            # print(i)
            yield i 

    num_gen = gen()
    # next commands gives us the return of just the next iteration (output: 0)
    print(next(num_gen))
    # (output: 1)
    print(next(num_gen))
    # (output: 2)
    print(next(num_gen))

    try: 
        print(next(num_gen))
        print(next(num_gen))
        print(next(num_gen))
        print(next(num_gen))
        print(next(num_gen))
        print(next(num_gen))
        print(next(num_gen))
        print(next(num_gen))
        print(next(num_gen))
        print(next(num_gen))
        print(next(num_gen))
        print(next(num_gen))
    except StopIteration:
        print('All Done!')

