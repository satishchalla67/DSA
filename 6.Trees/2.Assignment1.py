
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
def preorder_iterative(root):
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.data, end=' ')
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def inorder_iterative(root):
    stack = []
    curr = root
    while True:
        if curr:
            stack.append(curr)
            curr = curr.left
        elif stack:
            curr = stack.pop()
            print(curr.data, end=' ')
            curr = curr.right
        else:
            break
        
def postorder_iterative(root):
    s1 = [root]
    s2 = []
    while s1:
        curr = s1.pop()
        s2.append(curr)
        if curr.left:
            s1.append(curr.left)
        if curr.right:
            s1.append(curr.right)
    while s2:
        curr = s2.pop()
        print(curr.data, end=' ')
    
    
    
    
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.left.right = Node(7)
root.left.right.left = Node(8)
root.left.right.right = Node(9)

# preorder_iterative(root)
postorder_iterative(root)