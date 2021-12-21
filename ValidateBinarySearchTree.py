# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 00:52:09 2021

@author: zyang672
"""
from copy import deepcopy
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        elif not root.left and not root.right:
            return True

        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                break
            node = stack.pop()
            res.append(node.val)
            root = node.right
        a = deepcopy(res)
        res.sort()
        if a == res:
            return True
        else:
            return False
        
if __name__ == '__main__':
    p = TreeNode(5)
    p.left = TreeNode(1)
    p.right = TreeNode(4)
    p.right.left = TreeNode(3)
    p.right.right = TreeNode(6)
    q = [2,7,13,19]

#    q.right.right = TreeNode(0)
    print Solution().isValidBST(p)         