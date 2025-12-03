# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        def dfs(root1, root2, level):
            if root1 is None and root2 is None:
                return
            if level%2==1:
                root1.val, root2.val = root2.val, root1.val
            dfs(root1.left, root2.right,level+1)
            dfs(root1.right, root2.left,level+1)
        dfs(root.left, root.right,1)
        return root
        