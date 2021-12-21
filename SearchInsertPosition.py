# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 00:52:09 2021

@author: zyang672
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        left, right = 0, n-1
        
        if target < nums[0]:
            return 0
        if target > nums[right]:
            return n
        
        while left < right:
            mid = (right + left)/2 
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
                
        return left
            
        
if __name__ == '__main__':
    #p = TreeNode(1)
    #p.right, p.left = TreeNode(2), TreeNode(3)
    q = [1,3,5,6]
    #q.right, q.left = TreeNode(2), TreeNode(3)
#    q.right.right = TreeNode(0)
    print Solution().searchInsert([1], 0)         