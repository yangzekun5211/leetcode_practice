# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 00:52:09 2021

@author: zyang672
"""

# Definition for a binary tree node.

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def binerySearch(nums):
            n = len(nums)
            left, right = 0, n-1

            while left < right:
                mid = (left+right)/2
                if nums[mid] == 0:
                    return mid
                elif nums[mid] < 0:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        st = binerySearch(nums)
        l1 = [abs(i) for i in nums[:st][::-1]]
        l2 = nums[st:]
        res = []
        while l1 and l2:
            if l1[0] < l2[0]:
                res.append(l1[0]**2)
                l1.pop(0)
            else:
                res.append(l2[0]**2)
                l2.pop(0)
        if l1:
            res.extend([i**2 for i in l1])
        if l2:
            res.extend([i**2 for i in l2])
        return res
    
if __name__ == '__main__':
    p = -1
    q = [-4,-1,0,3,10]

#    q.right.right = TreeNode(0)
    print Solution().sortedSquares(q)         