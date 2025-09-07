# Insertion of BST
# search BST
# Deletion of BST(no child, one child, two child)


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insertBST(root, key):
    if root is None:
        return Node(key)
    elif root.val==key:
        return root
    else:
        if root.val<key:
            root.right = insertBST(root.right, key)
        else:
            root.left = insertBST(root.left, key)
    return root


def searchBST(root, key):
    if root is None:
        return None
    elif root.val == key:
        return root.val
    else:
        if root.val<key:
            return searchBST(root.right, key)
        else:
            return searchBST(root.left, key)
    

def deleteBST(root, key):
    if root is None:
        return None
    elif root.val<key:
        root.right = deleteBST(root.right, key)
    elif root.val>key:
        root.left = deleteBST(root.left, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            temp = root.right
            while temp.left:
                temp = temp.left
            root.val = temp.val
            root.right = deleteBST(root.right, temp.val)
    return root
          

def inOrder(root):
    if root:
        print(str(root.val), end=" ")
        inOrder(root.left)
        inOrder(root.right)
        
root = Node(50)
root = insertBST(root, 40)
root = insertBST(root, 30)
root = insertBST(root, 45)
root = insertBST(root, 60)
root = insertBST(root, 55)
root = insertBST(root, 65)


inOrder(root)
deleteBST(root, 50)
print()
inOrder(root)