import random
print(random.randint(1,1))


   """ def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        value = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front+1)%len(self._data)
        self._size -= 1
        if self._size <= Queue.K * len(self._data) and len(self._data) > Queue.DEFAULT_CAPACITY:
            if len(self._data) // 2 > Queue.DEFAULT_CAPACITY:
                self.resize(len(self._data) // 2)
            else:
                self.resize(Queue.DEFAULT_CAPACITY)
        return value"""
