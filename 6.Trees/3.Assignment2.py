class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def buildTree(predorder, inorder):    
    inorder_map = {element: idx for idx, element in enumerate(inorder)}
    
    
    def helper(pre_start, pre_end, in_start, in_end):
        
        if pre_start>pre_end or in_start>in_end:
            return None
        
        root_val = predorder[pre_start]
        root = Node(root_val)
        
        # find root index in inorder
        in_root = inorder_map[root_val]
        left_subtree_size = in_root - in_start
        
        root.left = helper(pre_start+1, pre_start+left_subtree_size, in_start, in_root-1)
        root.right = helper(pre_start+left_subtree_size+1, pre_end, in_root+1, in_end)
        
        return root
    
    return helper(0, len(predorder)-1, 0, len(inorder)-1)


# function to convert binary tree to list for visualization
def treeToList(root):
    if not root:
        return []
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result
    



preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
binarytree = buildTree(preorder, inorder)
print(treeToList(binarytree))