# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 00:52:09 2021

@author: zyang672
"""

# Definition for a binary tree node.

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        cur_s, cur_e = -1, -1
        for s, e in sorted(intervals, key=lambda x: x[0]):
            if s > cur_e:
                result.append([cur_s, cur_e])
                cur_s = s
                cur_e = e
            else:
                cur_e = max(cur_e, e)
        result.append([cur_s, cur_e])
        return result[1:]
    
if __name__ == '__main__':
    p = -1
    q = [2,7,13,19]

#    q.right.right = TreeNode(0)
    print Solution().convertToBase7(p)         