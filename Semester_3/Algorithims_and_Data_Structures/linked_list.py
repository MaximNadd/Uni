class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node

    def remove(self, value):
        current = self.head
        prev = None
        while current is not None:
            if current.value == value:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next
        raise ValueError(f"{value!r} not in list")

    def print(self):
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.value))
            current = current.next
        print(" -> ".join(values) if values else "(empty)")
