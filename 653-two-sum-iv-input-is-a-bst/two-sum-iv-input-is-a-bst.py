# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.s = set()
    def findTarget(self, root, k):
        if root == None:
            return False
        if root.val in self.s:
            return True
        else:
            self.s.add(k-root.val)
        return self.findTarget(root.left,k) or self.findTarget(root.right,k)
        