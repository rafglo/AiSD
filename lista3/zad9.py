import math

class Empty(Exception):
    pass

class Queue:
    DEFAULT_CAPACITY = 10
    K = 0.2

    def __init__(self):
        self._data = [None]*Queue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        value = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front+1)%len(self._data)
        self._size -= 1
        if self._size <= Queue.K * len(self._data):
            self.resize(len(self._data) // 2)
        return value

    def enqueue(self,e):
        if self._size == len(self._data):
            self.resize(2*len(self._data))
        avail = (self._front + self._size)%len(self._data)
        self._data[avail] = e
        self._size += 1

    def resize(self,cap):
        old = self._data
        self._data = [None]*cap
        walk = self._front
        for k in range(self._size): #only existing elements
            self._data[k] = old[walk]
            walk = (1 + walk)%len(old)
        self._front = 0 

    def __str__(self):
        """elements = [(self._data[(self._front + i) % len(self._data)]) for i in range(self._size)]
        return f"Queue: {elements}"
        """
        result = []
        for i in range(len(self._data)):
            if self._data[(self._front + i)%len(self._data)] is None:
                result.append(" ")
            else:
                result.append(self._data[(self._front + i)%len(self._data)])
        return str(result)
    
class Stack_using_queue():

    def __init__(self):
        self.queue = Queue()

    def __len__(self):
        return len(self.queue)
    
    def is_empty(self):
        return self.queue.is_empty()
    
    def push(self, value):
        self.queue.enqueue(value)
        for i in range(len(self.queue) - 1):
            val = self.queue.dequeue()
            self.queue.enqueue(val)
        
    def top(self):
        if self.is_empty:
            raise Empty("Stack is empty")
        else:
            return self.queue.first()
    
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        else:
            return self.queue.dequeue()
    
    def __str__(self):
        return str(self.queue)

s = Stack_using_queue()
s.push(4)
s.push(9)
s.pop()
print(s)

        
        
