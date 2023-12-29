import time

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped = self.top
        self.top = self.top.next
        popped.next = None
        return popped.data

    def top_element(self):
        return self.top.data if self.top else None

    def is_empty(self):
        return self.top is None

# Funkcja do przeprowadzenia analizy eksperymentalnej
def experimental_analysis(stack_size):
    stack = LinkedListStack()

    # Pomiar czasu dla operacji push
    start_time = time.time()
    for i in range(stack_size):
        stack.push(i)
    push_time = time.time() - start_time

    # Pomiar czasu dla operacji pop
    start_time = time.time()
    for _ in range(stack_size):
        stack.pop()
    pop_time = time.time() - start_time

    # Pomiar czasu dla operacji top
    start_time = time.time()
    for _ in range(stack_size):
        stack.top_element()
    top_time = time.time() - start_time

    return push_time, pop_time, top_time

# Przeprowadzenie analizy eksperymentalnej dla różnych rozmiarów stosu
stack_sizes = [10**3, 10**4, 10**5]
for size in stack_sizes:
    push_time, pop_time, top_time = experimental_analysis(size)
    print(f"Stack Size: {size}")
    print(f"Push Time: {push_time:.6f} seconds")
    print(f"Pop Time: {pop_time:.6f} seconds")
    print(f"Top Time: {top_time:.6f} seconds")
    print("="*30)


class BinaryTreeUsingArray():


    def __init__(self):
        self.data = [None] 
        self.size = 0
        self.root = 0

    def set_root(self, value):
        if self.data[self.root] is not None:
            raise RootError("Root already exists")
        else:
            self.data[self.root] = value
        self.data += [None, None]
        self.size += 1
    
    def add_left_child(self, parent_index, child_value):
        child_index = 2 * parent_index + 1
        if self.size == 1:
            self.data += [None] * 2
        elif len(self.data) < child_index:
            self.data += [None] * 2 * (len(self.data) - 1)
        if self.data[child_index] is not None:
            raise ChildError("Child already exists")
        else:
            self.data[child_index] = child_value
            self.size += 1
    
    def add_right_child(self, parent_index, child_value):
        child_index = 2 * parent_index + 2
        if self.size == 1:
            self.data += [None] * 2
        elif len(self.data) < child_index:
            self.data += [None] * 2 * (len(self.data)-1)
        if self.data[child_index] is not None:
            raise ChildError("Child already exists")
        else:
            self.data[child_index] = child_value
            self.size += 1

    def get_right_child(self, parent_index):
        child_index = 2 * parent_index + 2
        if self.data[child_index] is None:
            raise ChildError("Child doesn't exists")
        else:
            return self.data[child_index]
    
    def get_left_child(self, parent_index):
        child_index = 2 * parent_index + 1
        if self.data[child_index] is None:
            raise ChildError("Child doesn't exists")
        else:
            return self.data[child_index]
        
    def __str__(self):
        return str(self.data)