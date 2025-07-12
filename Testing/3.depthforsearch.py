
class Node:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


def buildTree(preorder, inorder):
    
    inorder_map = {element: index for index, element in enumerate(inorder)}
    
    def helper(pre_start, pre_end, in_start, in_end):
        if pre_start>pre_end or in_start>in_end:
            return None
        start_index = preorder[pre_start]
        root = Node(start_index)
        inorder_root_index = inorder_map[start_index]
        left_subtree_length = inorder_root_index - in_start
        
        root.left = helper(pre_start+1, pre_start+left_subtree_length, in_start, inorder_root_index-1)
        root.right = helper(pre_start+left_subtree_length+1, pre_end, inorder_root_index+1, in_end)
        return root
    return helper(0, len(preorder)-1, 0, len(inorder)-1)

# Depth first Search
def treeToList(root):
    stack = [root]
    res = []
    while stack:
        curr = stack.pop()
        res.append(curr.val)
        if curr.right:
            stack.append(curr.right)
        else:
            res.append(None)
        if curr.left:
            stack.append(curr.left)
        else:
            res.append(None)
    return res

    
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
binarytree = buildTree(preorder, inorder)
print(treeToList(binarytree))