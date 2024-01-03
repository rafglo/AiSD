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
        self.left_child = value

    def add_right_child(self, value):
        self.right_child = value

    def get_left_child(self):
        if self.has_left_child:
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
        if self.has_left_child() or self.has_right_child():
            return False
        else:
            return True
        
    def __str__(self):
        funcs = ['sin', 'cos', 'exp', 'log']
        ops = ['+', '-','*','/','^']
        if self.left_child is None:
            a = ""
        else:
            a = str(self.left_child)
        if self.right_child is None:
            b = ""
        else:
            b = str(self.right_child)
        if self.value in ops:
            return "("+a+str(self.value)+b+")"
        elif self.value in funcs:
            return str(self.value) + "(" + b + ")"
        else:
            return a+str(self.value)+b
    

def tokenize(raw):
    SYMBOLS = set('+-*^/() ') # allow for '*' or 'x' for multiplication
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


print(tokenize("(sin((4*x))/7)"))

def build_expression_tree(tokens):
    S = [] # we use Python list as stack
    funcs = ["sin", "cos", "exp", "log"]
    for t in tokens:
        if t in '+-*/^': # t is an operator symbol
            S.append(t) # push the operator symbol
        elif t not in '()': # consider t to be a literal
            if t in funcs:
                S.append(t)
            else:
                S.append(TreeNode(t)) # push trivial tree storing value
        elif t == ')': # compose a new tree from three constituent parts
            right = S.pop() # right subtree as per LIFO
            op = S.pop() # operator symbol
            if op in funcs:
                S.append(TreeNode(op, None, right))
            else:
                left = S.pop() # left subtree
                S.append(TreeNode(op, left, right)) # repush tree
            # we ignore a left parenthesis
    return S.pop()

print(build_expression_tree(tokenize("(sin(((x^2)+2))/2)")))

def derivative_on_tree(tree, var):
    if tree.is_leaf():
        if tree.value == var:
            return "1"
        else:
            return "0"
    else:
        if tree.value == '*':
            new_tree = TreeNode("+")
            new_tree.add_left_child(TreeNode('*', derivative_on_tree(tree.get_left_child(), var), tree.get_right_child()))
            new_tree.add_right_child(TreeNode('*', tree.get_left_child(), derivative_on_tree(tree.get_right_child(), var)))
            return new_tree
        elif tree.value == "+":
            new_tree = TreeNode("+")
            new_tree.add_left_child(derivative_on_tree(tree.get_left_child(),var))
            new_tree.add_right_child(derivative_on_tree(tree.get_right_child(),var))
            return new_tree
        elif tree.value == "-":
            new_tree = TreeNode("-")
            new_tree.add_left_child(derivative_on_tree(tree.get_left_child(),var))
            new_tree.add_right_child(derivative_on_tree(tree.get_right_child(),var))
            return new_tree
        elif tree.value == "/":
            new_tree = TreeNode("/")
            new_tree.add_left_child(TreeNode("-", TreeNode("*", derivative_on_tree(tree.get_left_child(), var), tree.get_right_child()), TreeNode("*", tree.get_left_child(), derivative_on_tree(tree.get_right_child(), var))))
            new_tree.add_right_child(TreeNode("*", tree.get_right_child(), tree.get_right_child()))
            return new_tree
        elif tree.value == "^":
            new_tree = TreeNode("*")
            new_tree.add_left_child(derivative_on_tree(tree.get_left_child(),var))
            new_tree.add_right_child(TreeNode("*",tree.get_right_child(),TreeNode("^",tree.get_left_child(),TreeNode("-",tree.get_right_child(),"1"))))
            return new_tree
        elif tree.value == "sin":
            new_tree = TreeNode("*")
            new_tree.add_left_child(derivative_on_tree(tree.get_right_child(), var))
            new_tree.add_right_child(TreeNode("cos", None, tree.get_right_child()))
            return new_tree
        elif tree.value == "cos":
            new_tree = TreeNode("*")
            new_tree.add_left_child(derivative_on_tree(tree.get_right_child(), var))
            new_tree.add_right_child(TreeNode("*", TreeNode("-", "0", "1"), TreeNode("sin", None, tree.get_right_child())))
            return new_tree
        elif tree.value == "exp":
            new_tree = TreeNode("*")
            new_tree.add_left_child(derivative_on_tree(tree.get_right_child(),var))
            new_tree.add_right_child(TreeNode("exp",None,tree.get_right_child()))
            return new_tree
        elif tree.value == "log":
            new_tree = TreeNode("*")
            new_tree.add_left_child(derivative_on_tree(tree.get_right_child(),var))
            new_tree.add_right_child(TreeNode("/","1",tree.get_right_child()))
            return new_tree

    
def derivative(expression, var):
    tokens = tokenize(expression)
    tree = build_expression_tree(tokens)
    return derivative_on_tree(tree, var)

print(derivative("(x + (sin((x^2)) / x))", "x"))