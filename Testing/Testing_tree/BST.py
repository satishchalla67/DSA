


class Node:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data
        
        
        

def insertion(root, key):
    if root is None:
        return Node(key)
    else:
        if root.data==key:
            return root
        elif root.data>key:
            root.left=insertion(root.left, key)
        else:
            root.right=insertion(root.right, key)
    return root

def searchBST(root, key):
    if root is None:
        return None
    if root.data==key:
        return root.data
    elif root.data>key:
        return searchBST(root.left, key)
    else:
        return searchBST(root.right, key)
    

def deleteBST(root, key):
    if root is None:
        return None
    if root.data>key:
        root.left=deleteBST(root.left, key)
    elif root.data<key:
        root.right=deleteBST(root.right, key)
    else:
        if root.right is None:
            return root.left
        elif root.left is None:
            return root.right
        else:
            temp=root.right
            while temp.left:
                temp=temp.left
            root.data=temp.data
            root.right=deleteBST(root.right, temp.data)

def treetolist(root):
    if root is None:
        return []
    result=[]
    queue=[root]
    while queue:
        node=queue.pop(0)
        if node:
            result.append(node.data)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result

root=Node(56)
insertion(root, 20)
insertion(root, 70)
insertion(root, 10)
insertion(root, 25)
insertion(root, 79)
insertion(root, 60)
print(treetolist(root))
deleteBST(root, 56)
print(treetolist(root))