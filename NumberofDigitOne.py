# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 00:52:09 2021

@author: zyang672
"""

# Definition for a binary tree node.

class Solution(object):
    '''
        def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
        digits = len(str(n))
        if digits == 1:
            return 1
        last_d = n/(10**(digits-1))
        result = (digits-1) * (10**(digits-2))
        if last_d == 1:
            result += n%(10**(digits-1)) + 1
        else:
            result += 10**(digits-1)
        if n%(10**(digits-1)):
            result += last_d*self.countDigitOne(n%(10**(digits-1)))
        else:
            result += (last_d-1) * (digits-1) * (10**(digits-2))
        return result
    '''
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
        digits = len(str(n))
        if digits == 1:
            return 1
        last_d = n/(10**(digits-1))
        result = last_d * (digits-1) * (10**(digits-2))
        if last_d == 1:
            result += n%(10**(digits-1)) + 1
        else:
            result += 10**(digits-1)
        if n%(10**(digits-1)):
            result += self.countDigitOne(n%(10**(digits-1)))
        '''
        else:
            result += (digits-1) * (10**(digits-2))
        '''
        return result
    
if __name__ == '__main__':
    p = 300
    q = [2,7,13,19]

#    q.right.right = TreeNode(0)
    print Solution().countDigitOne(p)         