# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfNodes(self, root) -> int:
        if not root:
            return 0
        left = self.sumOfNodes(root.left)
        right = self.sumOfNodes(root.right)
        
        return left+right+root.val
    
root=TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
res = Solution()
print(res.sumOfNodes(root))