# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 12:35:05 2021

@author: zyang672
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first, last = 0, len(nums)-1
        mid = (last + first) // 2
        while last >= first :
            if nums[mid] > target:
                last = mid - 1
            elif nums[mid] < target:
                first = mid + 1
            else:
                return mid
            mid = (last + first) // 2

        else:
            return -1
if __name__ == '__main__':
    p = 13
    q = [-1,0,3,5,9,12]

#    q.right.right = TreeNode(0)
    print Solution().search(q, p)         