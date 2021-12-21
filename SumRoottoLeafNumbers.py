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
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        cur_dict = {root: 0}
        next_dict = {}
        result = 0
        
        while len(cur_dict.keys()) > 0:
            for node in cur_dict.keys():
                path = node.val + 10*cur_dict[node]
                if not node.left and not node.right:
                    result += path
                if node.left:
                    next_dict[node.left] = path
                if node.right:
                    next_dict[node.right] = path
            cur_dict = next_dict
            next_dict = {}
        
        return result
        
if __name__ == '__main__':
    p = TreeNode(1)
    p.right= TreeNode(0)
    q = TreeNode(1)
    q.right, q.left = TreeNode(2), TreeNode(3)
#    q.right.right = TreeNode(0)
    print Solution().sumNumbers(p)         