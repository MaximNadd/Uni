class Deque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.deque = [None] * capacity   # pre‑allocate storage
        self.head = 0                   # index of first (leftmost) element
        self.tail = 0                   # index where next element goes
        self.size = 0                   # current number of elements

    def append_right(self, item):
        if self.size == self.capacity:
            print("ERROR OVERFLOW")
        else:
            self.deque[self.tail] = item
            self.tail = (self.tail + 1) % self.capacity
            self.size += 1

    def append_left(self, item):
        if self.size == self.capacity:
            print("ERROR OVERFLOW")
        else:
            self.head = (self.head - 1) % self.capacity
            self.deque[self.head] = item
            self.size += 1

    def pop_right(self):
        if self.size == 0:
            print("DEQUE EMPTY")
        else:
            self.tail = (self.tail - 1) % self.capacity
            item = self.deque[self.tail]
            self.size -= 1
            return item

    def pop_left(self):
        if self.size == 0:
            print("DEQUE EMPTY")
        else:
            item = self.deque[self.head]
            self.head = (self.head + 1) % self.capacity
            self.size -= 1
            return item

    def __repr__(self):
        if self.size == 0:
            print("DEQUE EMPTY")
        else: 
            items = []
            for i in range(self.size):
                idx = (self.head + i) % self.capacity
                items.append(repr(self.deque[idx]))
            return f"Deque([{', '.join(items)}])"

    def print_ele(self, idx):
        if self.size == 0:
            print("DEQUE EMPTY")
        elif idx >= 0 and idx <= self.size: 
            idx = (self.head + idx) % self.capacity
            print(self.deque[idx])
        else:
            print("INDEX OUT OF ORDER")


dq = Deque(3)
dq.append_left(10)
dq.append_left(20)
dq.append_right(5)

print("\n")

print(repr(dq))
dq.print_ele(2)               
         

dq.pop_right()
dq.pop_left()

print("\n")

print(repr(dq))
dq.print_ele(0)           
