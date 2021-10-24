class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

    def __str__(self):
        string_list = str(self.items)
        return string_list


q = Queue()

q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.dequeue()

print(q.is_empty())
print(q)
print(q.size())
