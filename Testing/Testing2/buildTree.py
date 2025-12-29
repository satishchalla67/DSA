


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
        
def buildTree(preorder, inorder):
    
    inorder_map = {element:index for index, element in enumerate(inorder)}
    
    
    def helper(pre_start, pre_end, in_start, in_end):
        
        if pre_start>pre_end or in_start>in_end:
            return None
        
        
        start_element = preorder[pre_start]
        start_index = inorder_map[start_element]
        
        root = Node(start_element)
        
        left_subarray_size = start_index - in_start
        
        root.left = helper(pre_start+1, pre_start+left_subarray_size, in_start, start_index-1)
        root.right = helper(pre_start+left_subarray_size+1, pre_end, start_index+1, in_end)
        
        return root
    
    return helper(0, len(preorder)-1, 0, len(inorder)-1) 



def treeToList(root):
    # Depth first search
    
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        curr = queue.pop(0)
        if curr:
            result.append(curr.val)
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