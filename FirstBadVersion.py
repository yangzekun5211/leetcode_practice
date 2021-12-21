# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 00:52:09 2021

@author: zyang672
"""

# Definition for a binary tree node.

class Solution(object):
    def firstBadVersion(self, num):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        n = len(num)
        right = n-1
        if n == 1:
            return 1
        
        while left < right:
            mid = (right + left)//2
            if num[mid]:
                right = mid
            else:
                left = mid + 1
                
        return left + 1
            
        
if __name__ == '__main__':
    #p = TreeNode(1)
    #p.right, p.left = TreeNode(2), TreeNode(3)
    q = [0, 1]
    #q.right, q.left = TreeNode(2), TreeNode(3)
#    q.right.right = TreeNode(0)
    print Solution().firstBadVersion(q)         