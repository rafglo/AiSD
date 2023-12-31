import math

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
    
def permutation(array):
    S1 = Stack()
    S2 = Stack()
        
    for i in range(len(array)):
        S1.push([array[i]])

    while True:

        while not S1.is_empty():
            cur_top = S1.top()
            for num in array:
                a = cur_top.copy()
                if not num in a:
                    a.append(num)
                    S2.push(a)
            S1.pop()

        if len(S1) == math.factorial(len(array)) and len(S1.top()) == len(array):
            return S1
        elif len(S2) == math.factorial(len(array)) and len(S2.top()) == len(array):
            return S2
        
        
        while not S2.is_empty():
            cur_top = S2.top()
            for num in array:
                a = cur_top.copy()
                if not num in a:
                    a.append(num)
                    S1.push(a)
            S2.pop()

        if len(S1) == math.factorial(len(array)) and len(S1.top()) == len(array):
            return S1
        elif len(S2) == math.factorial(len(array)) and len(S2.top()) == len(array):
            return S2
        


print(permutation([1,2,3,4]))
