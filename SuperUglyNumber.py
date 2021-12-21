# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 00:52:09 2021

@author: zyang672
"""

# Definition for a binary tree node.

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly = [1]
        cur = [0] * len(primes)
        i = 1
        #pre_ugly = 1
        while i < n:
            candidates = [primes[j]*ugly[cur[j]] for j in range(len(primes))]
            cur_ugly = min(candidates)
            ugly.append(cur_ugly)
            for j in range(len(primes)):
                if primes[j]*ugly[cur[j]] == cur_ugly:
                    cur[j] += 1
            i += 1
            
        return ugly[-1]
        
if __name__ == '__main__':
    p = 12
    q = [2,7,13,19]

#    q.right.right = TreeNode(0)
    print Solution().nthSuperUglyNumber(p, q)         