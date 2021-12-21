# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:47:37 2021

@author: zyang672
"""
# Consider it in the normal devision method

class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        def isSub(x, y):
            i = 0
            while len(x)+i <= len(y):
                if y[i:i+len(x)] == x:
                    return True
                i += 1
            return False
        m = len(b)/len(a)+2
        for i in range(1,m+1):
            if isSub(b, a*i):
                return i
            i += 1
        return -1
            
    
if __name__ == '__main__':
    p = "abc"
    q = "cabcabca"
#    q.right.right = TreeNode(0)
    print Solution().repeatedStringMatch(p, q)   