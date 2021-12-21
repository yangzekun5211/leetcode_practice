# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 00:52:09 2021

@author: zyang672
"""

# Definition for a binary tree node.

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        total_digits = 9
        #if n < total_digits:
        #    return n
        while n > total_digits:
            n -= total_digits
            i += 1
            total_digits = (10**i - 10**(i-1)) * i
        
        start = 10**(i-1)
        num = (n-1)/i + start 
        res = int(str(num)[(n-1)%i])
        return res
    
if __name__ == '__main__':
    p = 3
    q = [2,7,13,19]

#    q.right.right = TreeNode(0)
    print Solution().findNthDigit(p)         