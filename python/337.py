# 337. House Robber III
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) ->int:
        def dp(root):
            if not root:
                return (0,0)
            ml=dp(root.left)
            mr=dp(root.right)
            return (ml[1]+mr[1]+root.val, max(ml)+max(mr))
        return max(dp(root)))
