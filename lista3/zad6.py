class Empty(Exception):
    pass

class Deque():
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self.data = [None] * Deque.DEFAULT_CAPACITY
        self.size = 0
        self.front = 0
        self.end = self.size - 1

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def first(self):
        if self.is_empty:
            raise Empty("Deque is empty")
        else:
            return self.data[self.front]
    
    def last(self):
        if self.is_empty:
            raise Empty("Deque is empty")
        else:
            return self.data[self.end]
        
    def resize(self, cap):
        old = self.data
        new = [None] * cap
        walk = self.front
        for i in range(self.size):
            new[walk] = old[i]
            walk = (walk + i) % len(self.data)
        self.front = 0
        self.end = self.size - 1
        
    def add_first(self, item):
        if self.size == len(self.data):
            self.resize(2*len(self.data))
        avail = (self.front - 1) % len(self.data)
        self.data[avail] = item
        self.front = avail
        self.size += 1

    def add_last(self, item):
        if self.size == len(self.data):
            self.resize(2*len(self.data))
        avail = (self.front + self.size) % len(self.data)
        self.data[avail] = item
        self.end = avail
        self.size += 1

    def __str__(self):
        """elements = [(self._data[(self._front + i) % len(self._data)]) for i in range(self._size)]
        return f"Queue: {elements}"
        """
        result = []
        for i in range(len(self.data)):
            if self.data[(self.front + i)%len(self.data)] is None:
                result.append(" ")
            else:
                result.append(self.data[(self.front + i)%len(self.data)])
        return str(result)
    
    def delete_first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return value
    
    def delete_last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        value = self.data[self.end]
        self.data[self.end] = None
        self.end = (self.end - 1) % len(self.data)
        self.size -= 1
        return value 
    
d = Deque()
d.add_first(1)
d.add_last(3)
d.add_first(5)
d.add_last(8)
d.delete_first()
d.delete_last()
d.delete_first()
print(d)