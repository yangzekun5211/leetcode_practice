# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 00:52:09 2021

@author: zyang672
"""

# Definition for a binary tree node.

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        l = len(nums1)
        m -= 1
        n -= 1
        for i in range(l-1, -1, -1):
            if m>-1 and n>-1:
                if nums1[m] > nums2[n]:
                    nums1[i] = nums1[m]
                    m -= 1
                else:
                    nums1[i] = nums2[n]
                    n -= 1
            elif n>-1:
                nums1[i] = nums2[n]
                n -= 1
            else:
                break
    
if __name__ == '__main__':
    p = [1,2,3,0,0,0]
    q = [2,5,6]

#    q.right.right = TreeNode(0)
    print Solution().merge(p,3,q,3)         