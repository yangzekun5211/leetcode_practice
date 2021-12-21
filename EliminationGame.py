# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:47:37 2021

@author: zyang672
"""
# Consider it in the normal devision method
class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n/2 == 0:
            return n
        i = 1
        res = 1
        m = n/2
        while i <= m:
            if not i%2:                
                res += 4**((i/2)-1)
            i += 1
        return res
    
if __name__ == '__main__':
    p = 4
    q = 9
#    q.right.right = TreeNode(0)
    print Solution().lastRemaining( 2)   