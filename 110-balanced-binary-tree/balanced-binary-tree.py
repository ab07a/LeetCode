# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        if root is None:
            return True
        def dfs(root, level):
            if root is None:
                return level-1
            ll = dfs(root.left, level+1)
            lr = dfs(root.right, level+1)
            if ll and lr and abs(ll-lr)<2:
                return max(ll,lr)
            return False
        return True if dfs(root,1) else False
        