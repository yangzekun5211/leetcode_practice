# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 00:52:09 2021

@author: zyang672
"""

# Definition for a binary tree node.

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x:
            return 0
        if x < 4:
            return 1
        if x == 4:
            return 2
        
        left = 1
        right = x/2
        while left < right:
            mid = (left+right)/2
            cur = mid * mid
            if cur == x:
                return mid

            if cur > x:
                right = mid
            elif mid == left:
                return mid
            else:
                left = mid
        return left
                
    
if __name__ == '__main__':
    p = -1
    q = [2,7,13,19]

#    q.right.right = TreeNode(0)
    print Solution().mySqrt(5)         