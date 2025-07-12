class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def insertBST(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val>key:
            root.left = insertBST(root.left, key)
        else:
            root.right = insertBST(root.right, key)
    return root


def inorder(root):
    if root is None:
        return None
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
        


def deletion(root, key):
    if root is None:
        return None
    if root.val < key: # move right 
        root.right = deletion(root.right, key)
    elif root.val > key: # move left
        root.left = deletion(root.left, key)  
    else:
        if root.left is None: # Node with single child, replace with right node
            return root.right
        elif root.right is None: # Node with single child
            return root.left
        else: # Node with both children
            # aim to find the smallest val from the right subtree and replace it with root
            temp = root.right # Move right
            while temp.left:  # go untill the left most node, which will be the smallest val
                temp = temp.left
            root.val = temp.val # replace the root with smallest val
            root.right = deletion(root.right, temp.val) # delete that last node, key will be temp.val
    return root


root = Node(50)
root = insertBST(root, 40)
root = insertBST(root, 70)
root = insertBST(root, 60)
root = insertBST(root, 80)
inorder(root)
print()
root = deletion(root, 50)
inorder(root)
print()