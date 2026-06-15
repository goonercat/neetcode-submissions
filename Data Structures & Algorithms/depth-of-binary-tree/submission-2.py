# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #iterative dfs using stack
        #dfs without recursion
        if not root:
            return 0
        
        stk = [[root,1]]
        l = 0
        while stk:
            [node,lvl] = stk.pop()
            if node.right:
                stk.append([node.right,lvl+1])
            if node.left:
                stk.append([node.left,lvl+1])
            l = max(l,lvl)
        
        return l