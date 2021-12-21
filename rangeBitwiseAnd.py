# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:47:37 2021

@author: zyang672
"""
# Consider it in the normal devision method

class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if right - left >= left:
            return 0
        if right == left:
            return right
        def int2bin(num):
            res = ""
            while num:
                dgt = str(num % 2)
                res = dgt + res
                num = num / 2
            return res
        l = int2bin(left)
        r = int2bin(right)
        l = "0"*(len(r)-len(l)) + l
        i = 0
        res = 0
        while i<len(l) and l[i] ==  r[i]:
            res = res*2 + int(l[i])
            i += 1
        res = res*(2**(len(r)-i))
        
        return res
    
if __name__ == '__main__':
    p = 4
    q = 5
#    q.right.right = TreeNode(0)
    print Solution().rangeBitwiseAnd(p, q)   