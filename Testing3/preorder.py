




class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
        
def preorder(root):
    stack = [root]
    
    while stack:
        curr = stack.pop()
        print(curr.data, end=" ")
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
def inorder(root):
    pass
    
        
        
root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.left = Node('F')
root.right.right = Node('G')

preorder(root)