# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 00:52:09 2021

@author: zyang672
"""

# enumerate + biscet.

class Solution(object):

    def findRightInterval(self, intervals):
        ints = sorted([[j,k,i] for i,[j,k] in enumerate(intervals)])
        begs = [i for i,_,_ in ints]
        out = [-1]*len(begs)
        for i,j,k in ints:
            t = bisect.bisect_left(begs, j)
            if t < len(begs):
                out[k] = ints[t][2]
        
        return out
    
if __name__ == '__main__':
    p = 3
    q = [[2,7],[13,19]]

#    q.right.right = TreeNode(0)
    print Solution().findRightInterval(q)         