class RootError(Exception):
    pass

class ChildError(Exception):
    pass

class ParentError(Exception):
    pass

class NodeError(Exception):
    pass

class TreeNode:

    def __init__(self, value, left_child=None, right_child=None):
        self.value = value              # string, stored value
        self.left_child = left_child    # None or TreeNode instance
        self.right_child = right_child  # None or TreeNode instance

    def get_value(self):
        return self.value

    def add_left_child(self, value):
        self.left_child(TreeNode(value))

    def add_right_child(self, value):
        self.add_right_child(TreeNode(value))

    def get_left_child(self):
        if self.has_left_child is not None:
            return self.left_child
        else:
            raise ChildError("Left child doesn't exist")

    def get_right_child(self):
        if self.has_right_child:
            return self.right_child
        else:
            raise ChildError("Right child doesn't exist")

    def has_left_child(self) -> bool:
        if self.left_child is not None:
            return True
        else:
            return False

    def has_right_child(self) -> bool:
        if self.right_child is not None:
            return True
        else:
            return False

    def is_leaf(self) -> bool:
        if self.has_left_child or self.has_right_child:
            return True
        else:
            return False

    def __str__(self):
        return str(self.value)
    

def tokenize(raw):
    SYMBOLS = set('+-x*/() ') # allow for '*' or 'x' for multiplication
    mark = 0
    tokens = []
    n = len(raw)
    for j in range(n):
        if raw[j] in SYMBOLS:
            if mark != j:
                tokens.append(raw[mark:j]) # complete preceding token
            if raw[j] != ' ':
                tokens.append(raw[j]) # include this token
            mark = j+1 # update mark to being at next index
    if mark != n:
        tokens.append(raw[mark:n]) # complete preceding token
    return tokens

def build_expression_tree(tokens):
    S = [] # we use Python list as stack
    for t in tokens:
        if t in '+-x*/': # t is an operator symbol
            S.append(t) # push the operator symbol
        elif t not in '()': # consider t to be a literal
            S.append(TreeNode(t)) # push trivial tree storing value
        elif t == ')': # compose a new tree from three constituent parts
            right = S.pop() # right subtree as per LIFO
            op = S.pop() # operator symbol
            left = S.pop() # left subtree
            S.append(TreeNode(op, left, right)) # repush tree
            # we ignore a left parenthesis
    return S

def derivative(expression):
    tokens = tokenize(expression)
    tree = build_expression_tree(tokens)
    

derivative("((5+4)*7)/9")