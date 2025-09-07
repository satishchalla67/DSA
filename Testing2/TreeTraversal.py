







class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        


def preOrder(root):
    if root:
        print(str(root.val), end=" ")
        preOrder(root.left)
        preOrder(root.right)
    return None


def inOrder(root):
    if root:
        inOrder(root.left)
        print(str(root.val), end=" ")
        inOrder(root.right)
    return None

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(str(root.val), end=" ")
    return None



root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.left = Node('F')


preOrder(root)
print()
inOrder(root)
print()
postOrder(root)