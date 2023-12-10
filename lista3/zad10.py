class Empty(Exception):
 pass

class Stack:
    def __init__(self):
        self._data = [] #nowy pusty stos

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data)==0

    def push(self,e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop() 
    
    def __str__(self):
        return str(self._data)
    
class Queue_using_two_stacks():

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def is_empty(self):
        return self.s1.is_empty() 

    def enqueue(self, value):
        for i in range(len(self.s1)):
            self.s2.push(self.s1.pop())
        self.s1.push(value)
        for i in range(len(self.s2)):
            self.s1.push(self.s2.pop())
    
    def dequeue(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        else:
            self.s1.pop()
    
    def __len__(self):
        return(len(self.s1))

    def first(self):
        return self.s1.top()
        
    def __str__(self):
        return str(self.s1)

        
a = Queue_using_two_stacks()
a.enqueue(2)
a.enqueue(3)
print(a)
a.enqueue(4)
print(a)
print(a.first())
a.dequeue()
print(a)

