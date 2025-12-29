

class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
        

def insertion(root, key):
    if root is None:
        return Node(key)
    if root.data==key:
        return root
    if root.data>key:
        root.left=insertion(root.left,key)
    else:
        root.right=insertion(root.right,key)
    return root

def searchBST(root,key):
    if root is None:
        return None
    if root.data==key:
        return root
    else:
        if root.data>key:
            return searchBST(root.left,key)
        else:
            return searchBST(root.right,key)


def deleteBST(root,key):
    if root is None:
        return None
    if root.data>key:
        root.left=deleteBST(root.left,key)
    if root.data<key:
        root.right=deleteBST(root.right,key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            temp=root.right
            while temp.left:
                temp=temp.left
            root.data=temp.data
            root.right=deleteBST(root.right, temp.data)
    return root
        
















def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)



root=Node(50)
root=insertion(root,60)
root=insertion(root,40)
root=insertion(root,80)
root=insertion(root,70)
inorder(root)
root=deleteBST(root, 50)
print()
inorder(root)
