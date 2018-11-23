import sys

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def  enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        self.items.pop()
    
    def size(self):
        return len(self.items)

    def printqueue(self):
        for items in self.items:
            print(items,)

q = Queue()
print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.printqueue()
q.dequeue()
print("\n")
q.printqueue()

