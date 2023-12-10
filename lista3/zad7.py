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
    voids = ["hr", "area", "base", "br", "col", "command", "embed", "img", "input", "keygen", "link", "meta", "param", "source", "track", "wbr", "img"]
    left_o = "<"
    right = ">"
    S = Stack()
    for i in range(len(text) - 1):
        if text[i] == left_o and text[i+1] != "/" and text[i+1] != "!":
            tag_name = ""
            j = i + 1
            while text[j] != right and text[j] != " ":
                tag_name += text[j].lower()
                j += 1
            else:
                if not tag_name in voids:
                    if tag_name[:11] != "view-source":
                        S.push(tag_name)

        elif text[i] == left_o and text[i+1] == "/" and text[i+1] != "!":
            tag_name = ""
            j = i + 2
            while text[j] != right and text[j] != " ":
                tag_name += text[j].lower()
                j += 1
            else:
                if tag_name == S.top():
                    S.pop()

    if S.is_empty():
        return True
    else:
        return S
    

print(tag_checker(sample2))



