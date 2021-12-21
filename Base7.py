# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 00:52:09 2021

@author: zyang672
"""

# Definition for a binary tree node.

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num <= 0:
            flag = -1
        else:
            flag = 1
            
        num = abs(num)
        i = 1
        if num < 7:
            res = str(num)
            if flag == -1:
                res = "-" + res
            return res
        while num >= 7**i:
            i += 1
        i -= 1
        res = ""
        while i > 0:
            digit = num/(7**i)
            res += str(digit) 
            num -= digit*(7**i)
            i -= 1
        res += str(num)
        if flag == -1:
            res = "-" + res
        return res
    
if __name__ == '__main__':
    p = -1
    q = [2,7,13,19]

#    q.right.right = TreeNode(0)
    print Solution().convertToBase7(p)         