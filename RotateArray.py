# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 00:52:09 2021

@author: zyang672
"""

# Definition for a binary tree node.

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        
        res = nums[-k:]
        
        res.extend(nums[:len(nums)-k])
        
        nums[:] = res
    
if __name__ == '__main__':
    p = 3
    q = [1,2,3,4,5,6,7]

#    q.right.right = TreeNode(0)
    print Solution().rotate(q,p)         