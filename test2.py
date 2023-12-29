class RootError(Exception):
    pass

class ChildError(Exception):
    pass

class ParentError(Exception):
    pass

class BinaryTreeUsingArray():


    def __init__(self):
        self.data = [None] 
        self.size = 0
        self.root = 0
        self.depth = 0

    def set_root(self, value):
        if self.data[self.root] is not None:
            raise RootError("Root already exists")
        else:
            self.data[self.root] = value
        self.size += 1
        self.depth += 1
    
    def add_left_child(self, parent_index, child_value):
        if self.data[parent_index] is None:
            raise ParentError("Parent doesn't exist")
        else:
            child_index = 2 * parent_index + 1
            if self.size == 1:
                self.data += [None] * 2
                self.depth += 1
            elif len(self.data) - 1 < child_index:
                self.data += [None] * 2 ** self.depth
                self.depth += 1
            if self.data[child_index] is not None:
                raise ChildError("Child already exists")
            else:
                self.data[child_index] = child_value
                self.size += 1
    
    def add_right_child(self, parent_index, child_value):
        if self.data[parent_index] is None:
            raise ParentError("Parent doesn't exist")
        else:
            child_index = 2 * parent_index + 2
            if self.size == 1:
                self.data += [None] * 2
                self.depth += 1
            elif len(self.data) - 1 < child_index:
                self.data += [None] * 2 ** self.depth
                self.depth += 1
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
    
d = BinaryTreeUsingArray()
d.set_root(1)
d.add_left_child(0,2)
d.add_right_child(0,4)
d.add_left_child(1,6)
d.add_right_child(3,8)
d.add_left_child(2, 5)
d.add_left_child(4, 7)
print(d)
print(len(d.data))