
class Node:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data



def buildTree(preorder, inorder):
    inorder_indexMap = {element: idx for idx, element in enumerate(inorder)}
    
    def helper(pre_start, pre_end, in_start, in_end):
        if pre_start>pre_end or in_start>in_end:
            return None
        
        start = preorder[pre_start]
        root = Node(start)
        inorder_root_index = inorder_indexMap[start]
        left_subtree_size = inorder_root_index - in_start
        
        root.left = helper(pre_start+1, pre_start+left_subtree_size, in_start, inorder_root_index-1)
        root.right = helper(pre_start+left_subtree_size+1, pre_end, inorder_root_index+1, in_end)
        return root
    
    return helper(0, len(preorder)-1, 0, len(inorder)-1)

def treeToList(root):
    if not root:
        return []
    queue = [root]
    result = []
    while queue:
        curr = queue.pop(0)
        if curr:
            result.append(curr.data)
            queue.append(curr.left)
            queue.append(curr.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result
    
    
    


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
binarytree = buildTree(preorder, inorder)
print(treeToList(binarytree))