

class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None




def constructBST(preorder, inorder):
    inorder_map = {element:idx for idx,element in enumerate(inorder)}
    
    def helper(pre_start, pre_end, in_start, in_end):
        if pre_start>pre_end or in_start>in_end:
            return None
        
        start=preorder[pre_start]
        root=Node(start)
        index_of_root=inorder_map[start]
        left_subtree_length=index_of_root-pre_start
        
        root.left=helper(pre_start+1, pre_start+left_subtree_length, in_start, index_of_root-1)
        root.right=helper(pre_start+left_subtree_length+1, pre_end, index_of_root+1, in_end)
        return root
    return helper(0, len(preorder)-1, 0, len(inorder)-1)

def treetolist(root):
    res=[]
    queue=[root]
    while queue:
        curr=queue.pop(0)
        if curr:
            res.append(curr.data)
            queue.append(curr.left)
            queue.append(curr.right)
        else:
            res.append(None)
    while res and res[-1] is None:
        res.pop()
    return res





preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
root=constructBST(preorder, inorder)
print(treetolist(root))