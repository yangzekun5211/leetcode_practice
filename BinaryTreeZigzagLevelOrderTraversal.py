# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 00:52:09 2021

@author: zyang672
"""
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right                                                                
from copy import deepcopy
# Definition for a binary tree node.
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = [[root.val]]
        stack = [root]
        lev = 0
        nex = []
        while stack or nex:
            if not stack:
                lev += 1
                vals = [n.val for n in nex]
                if lev%2:
                    vals = vals[::-1]
                res.append(vals)
                stack = nex
                nex = []
            else:
                node = stack.pop(0)
                if node.left:
                    nex.append(node.left)
                if node.right:
                    nex.append(node.right)
        return res
                
        
if __name__ == '__main__':
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    #p.right.left = TreeNode(15)
    p.right.right = TreeNode(5)
    p.left.left = TreeNode(4)
#    p.left.right = TreeNode(4)
    q = [2,7,13,19]

#    q.right.right = TreeNode(0)
    print Solution().zigzagLevelOrder(p)         