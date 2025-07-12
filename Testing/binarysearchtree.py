

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
def insertBST(root, key):
    if root is None:
        return Node(key)
    if root.val==key:
        return root
    elif root.val>key:
        root.left = insertBST(root.left, key)
    else:
        root.right = insertBST(root.right, key)
    return root


def inorder(root):
    curr = root
    stack = []
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
        
def deletion(root, key):
    if root is None:
        return None
    if root.val > key:
        root.left = deletion(root.left, key)
    elif root.val< key:
        root.right = deletion(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        else:
            temp = root.right
            while temp.left:
                temp = temp.left
            root.val = temp.val
            root.right = deletion(root.right, temp.val)
    return root

def searchBST(root, key):
    if root:
        if root.val==key:
            return True
        if root.val>key:
            return searchBST(root.left, key)
        else:
            return searchBST(root.right, key)
    return False


root = Node(50)
root = insertBST(root, 40)
root = insertBST(root, 70)
root = insertBST(root, 60)
root = insertBST(root, 80)
inorder(root)
print()
root = deletion(root, 70)
inorder(root)
print()
print(searchBST(root, 50))
            