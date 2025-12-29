class Node:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None


def preorder(root):
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")






root = Node('A')
root.left=Node('B')
root.right=Node('C')
root.left.left=Node('D')
root.left.right=Node('E')
root.right.left=Node('F')
preorder(root)
print()
inorder(root)
print()
postorder(root)







