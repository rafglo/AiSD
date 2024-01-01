class RootError(Exception):
    pass

class ChildError(Exception):
    pass

class ParentError(Exception):
    pass
class NodeError(Exception):
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
        
    def has_left_child(self, parent_index):
        child_index = 2 * parent_index + 1
        if child_index > len(self.data):
            return False
        else:
            if self.data[child_index] is None:
                return False
            else:
                return True
        
    def has_right_child(self, parent_index):
        child_index = 2 * parent_index + 2
        if child_index > len(self.data):
            return False
        else:
            if self.data[child_index] is None:
                return False
            else:
                return True
        
    def remove_node(self, index):
        if index > len(self.data):
            raise IndexError("Nie istnieje node o podanym indeksie")
        elif self.data[index] == None:
            raise NodeError("Nie istnieje node o podanym indeksie")
        else:
            family = [index]
            cur_index = 0
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            while left_child_index < len(self.data) - 1:
                family.append(left_child_index)
                family.append(right_child_index)
                cur_index += 1
                left_child_index = 2 * family[cur_index] + 1
                right_child_index = 2 * family[cur_index] + 2
            for i in family:
                self.data[i] = None

    def __str__(self):
        return str(self.data)
    
d = BinaryTreeUsingArray()
d.set_root(1)
d.add_left_child(0,2)
d.add_right_child(0,4)
d.add_left_child(1,6)
d.add_right_child(3,8)
d.add_left_child(2, 5)
d.add_right_child(5,10)
d.remove_node(2)
print(d)
print(len(d.data))
