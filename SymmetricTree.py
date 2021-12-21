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
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root.right and not root.left:
            return True
        if not root.left or not root.left:
            return False
        
        stack = [root]
        nex = []
        nex_val = []
        while stack or nex:
            if not stack:
                if nex_val != nex_val[::-1] or len(nex)%2:
                    return False
                stack = nex
                nex = []
                nex_val = []
            else:
                node = stack.pop()
                if node.left:
                    nex.append(node.left)
                    nex_val.append(node.left.val)
                elif not node.left:
                    nex_val.append(-101)
                if node.right:
                    nex.append(node.right)
                    nex_val.append(node.right.val)
                elif not node.right:
                    nex_val.append(-101)
        return True
        
if __name__ == '__main__':
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(2)
    p.right.left = TreeNode(4)
    p.right.right = TreeNode(3)
    p.left.left = TreeNode(3)
    p.left.right = TreeNode(4)
    q = [2,7,13,19]

#    q.right.right = TreeNode(0)
    print Solution().isSymmetric(p)         