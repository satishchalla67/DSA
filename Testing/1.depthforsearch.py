
class Node:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val
        
        
def preorder(root):
    if root:
        print(str(root.val), end=' ')
        preorder(root.left)
        preorder(root.right)
    return root        

def inorder(root):
    if root:
        preorder(root.left)
        print(str(root.val), end=' ')
        preorder(root.right)
    return root

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val), end=' ')
    return root
        
        
        
root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.left = Node('F')
preorder(root)
print()
inorder(root)
print()
postorder(root)
