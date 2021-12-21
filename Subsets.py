# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 00:52:09 2021

@author: zyang672
"""

# Definition for a binary tree node.
from copy import deepcopy
class Solution(object):
    def helper(self, rest, sub):
        self.result.extend(deepcopy(sub))
        if not rest:
            return
        else:
            sub = []
            for i in self.result:
                sub.append(i+[rest[0]])
            self.helper(rest[1:], sub)
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self.helper(nums, [[]])
        return self.result
                
    
if __name__ == '__main__':
    p = -1
    q = [1,2,3]

#    q.right.right = TreeNode(0)
    print Solution().subsets(q)         