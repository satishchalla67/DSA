
class Node:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


# Insertion of BST - O(logn)
def insertBST(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val==key:
            return root
        elif root.val<key:
            root.right = insertBST(root.right, key)
        else:
            root.left = insertBST(root.left, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val), end=' ')
        inorder(root.right)
        
# Search BST - O(logn)
def searchBST(root, key):
    if root:
        if root.val == key:
            return True
        elif root.val<key:
            return searchBST(root.right, key)
        else:
            return searchBST(root.left, key)
    return False

root = Node(50)
root = insertBST(root, 40)
root = insertBST(root, 70)
root = insertBST(root, 60)
root = insertBST(root, 80)
inorder(root)
print()
print(searchBST(root, 100))