import random
a= ""
b = "t"
a = a + "t"
print(a)


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

sample1 = open(r"C:\Users\Rafal\OneDrive\Dokumenty\GitHub\AiSD\lista3\HTML_sample1.txt").read()
sample2 = open(r"C:\Users\Rafal\OneDrive\Dokumenty\GitHub\AiSD\lista3\HTML_sample2.txt").read()
sample3 = open(r"C:\Users\Rafal\OneDrive\Dokumenty\GitHub\AiSD\lista3\HTML_sample3.txt").read()


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
    
def tag_checker(text):
    voids = ["hr", "area", "base", "br", "col", "command", "embed", "img", "input", "keygen", "link", "meta", "param", "source", "track", "wbr", "img", "view-source"]
    left_o = "<"
    right = ">"
    S = Stack()
    for i in range(len(text) - 1):
        if text[i] == left_o and text[i+1] != "/" and text[i+1] != "!":
            tag_name = ""
            j = i + 1
            while text[j] != right and text[j] != " ":
                tag_name += text[j]
                j += 1
            else:
                S.push(tag_name)
                    
        elif text[i] == left_o and text[i+1] == "/" and text[i+1] != "!":
            tag_name = ""
            j = i + 2
            while text[j] != right and text[j] != " ":
                tag_name += text[j]
                j += 1
            else:
                if tag_name == S.top():
                    S.pop()
        elif text[i] == left_o and text[i+1] == "!":
            j = i + 1
            while text[j] != right and text[j] != " ":
                if text[j] == left_o:
                    return False
                j += 1

    for k in range(len(S)):
        if S.top() in voids or S.top()[:11] == "view-source":
            S.pop()
    
    if S.is_empty():
        return True
    else:
        print(S)

s = Stack()
s.push(4)
s.push(9)
s.pop()
print(s)

print(list(range(3)))


