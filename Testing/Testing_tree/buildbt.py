
class Node:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data


def buildTree(preorder, inorder):
    
    inorder_index = {element: index for index,element in enumerate(inorder) }
    
    def helper(prestart, preend, instart, inend):
        if prestart>preend or instart>inend:
            return None        
        start=preorder[prestart]
        start_index=inorder_index[start]
        root=Node(start)
        left_subarray_length=start_index-prestart
        
        root.left=helper(prestart+1, prestart+left_subarray_length, instart, start_index-1)
        root.right=helper(prestart+left_subarray_length+1, preend, start_index+1, inend)
        return root
    return helper(0, len(preorder)-1, 0, len(inorder)-1)

def treetolist(root):
    if not root:
        return []
    stack=[root]
    res=[]
    while stack:
        curr = stack.pop(0)
        if curr:
            res.append(curr.data)
            stack.append(curr.left)
            stack.append(curr.right)
        else:
            res.append(None)
    while res and res[-1] is None:
        res.pop()
    return res

preorder=[3,9,20,15,17]
inorder=[9,3,15,20,17]
root=buildTree(preorder, inorder)
res=treetolist(root)
print(res)