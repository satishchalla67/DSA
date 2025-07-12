
class Node:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data
        


def preorder(root):
    if root:
        print(str(root.data), end=' ')
        preorder(root.left)
        preorder(root.right)
    return root

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.data), end=' ')
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.data), end=' ')
        inorder(root.right)
    return root 



root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.left = Node('F')
preorder(root)
print()
postorder(root)
print()
inorder(root)