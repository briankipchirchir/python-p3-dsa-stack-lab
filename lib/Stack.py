class Stack:
    def __init__(self, items=None, limit=None):
        if items is None:
            items = []
        self.items = items  # Renamed to 'items' to match test
        self.limit = limit

    def push(self, value):
        if self.limit is None or len(self.items) < self.limit:
            self.items.append(value)
        else:
            raise OverflowError("Stack is full")

    def pop(self):
        if self.isEmpty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def isEmpty(self):  # Renamed to match test
        return len(self.items) == 0

    def full(self):
        return self.limit is not None and len(self.items) == self.limit

    def search(self, value):
        if value in self.items:
            return len(self.items) - 1 - self.items.index(value)
        return -1
