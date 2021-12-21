# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 00:52:09 2021

@author: zyang672
"""

# Definition for a binary tree node.

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        binary = ["0", "1"]
        for i in range(1, n):
            upper = ["0"+j for j in binary]
            lower = ["1"+j for j in binary[::-1]]
            upper.extend(lower)
            binary = upper
            
        res = [self.bin2int(i) for i in binary]
        return res
        
    def bin2int(self, s):
        res = sum([int(s[i])*(2**(len(s)-i-1)) for i in range(len(s))])
        return res
    
if __name__ == '__main__':
    p = 3
    q = [2,7,13,19]

#    q.right.right = TreeNode(0)
    print Solution().grayCode(p)         