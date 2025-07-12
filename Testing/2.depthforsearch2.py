
class Node:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

def preorder(root):
    stack = [root]
    while stack:
        curr = stack.pop()
        print(str(curr.val), end=' ')
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    return root

def inorder(root):
    stack = []
    curr = root
    while True:
        if curr:
            stack.append(curr)
            curr = curr.left
        elif stack:
            curr = stack.pop()
            print(str(curr.val), end=' ')
            curr = curr.right
        else:
            break

def postorder(root):
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
        print(str(curr.val), end=' ')
        
        
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









