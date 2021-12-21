# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 00:52:09 2021

@author: zyang672
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def tree2list(root):
            stack = [root]
            l = []
            while stack:
                node = stack.pop(0)
                if node.left:
                    l.append(node.left.val)
                    stack.append(node.left)
                if not node.left:
                    l.append("null")
                if node.right:
                    l.append(node.right.val)
                    stack.append(node.right)
                if not node.right:
                    l.append("null")
            return l
        
        l_p = tree2list(p)
        l_q = tree2list(q)
        return l_p == l_q
        
if __name__ == '__main__':
    p = TreeNode(1)
    p.right, p.left = TreeNode(2), TreeNode(3)
    q = TreeNode(1)
    q.right, q.left = TreeNode(2), TreeNode(3)
#    q.right.right = TreeNode(0)
    print Solution().isSameTree(p, q)         