




class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
        


def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
        
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")
        
# ABDECF
# DBEAFC
# DEBFCA



root = Node('A')
root.left=Node('B')
root.right=Node('C')
root.left.left = Node('D')
root.left.right=Node('E')
root.right.left=Node('F')
preorder(root)
print()
inorder(root)
print()
postorder(root)
print()
