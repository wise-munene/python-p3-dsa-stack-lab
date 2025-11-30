class Stack:

    def __init__(self, items=None, limit=100):
        self.items = items if items is not None else []
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
        # Ignore the push completely
            pass
    def pop(self):
        if self.isEmpty():
            return None  
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        #
        return len(self.items) >= self.limit

    def search(self, target):
        if target not in self.items:
            return -1

        idx = self.items.index(target)
        return len(self.items) - 1 - idx
