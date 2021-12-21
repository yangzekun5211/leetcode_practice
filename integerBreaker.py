# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 00:52:09 2021

@author: zyang672
"""

# Definition for a binary tree node.

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 2
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        res = 0
        while i <= n/2:
            small = n/i
            num_small = i - n%i
            cur = (small**num_small) * ((small+1)**(i-num_small))
            res = max(res, cur)
            i += 1
        return res
    
if __name__ == '__main__':
    p = 55
    q = [2,7,13,19]

#    q.right.right = TreeNode(0)
    print Solution().integerBreak(p)         