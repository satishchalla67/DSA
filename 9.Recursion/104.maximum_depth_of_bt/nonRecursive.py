# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        q = [root]
        n=0
        while q:
            for i in range(len(q)): #difference between Breadth-First Search (BFS) for traversal versus BFS for levels.
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            n+=1
        return n
    
root=TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
res = Solution()
print(res.maxDepth(root))