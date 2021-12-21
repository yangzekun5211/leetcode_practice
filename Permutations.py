# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:47:37 2021

@author: zyang672
"""
# Consider it in the normal devision method
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        path = []
        res = []
        n = len(nums)
        self.helper(nums, res, path)
        return res
        
    def helper(self, nums, res, path):
        if not nums:
            res.append(path)
            return
        else:
            for i in range(len(nums)):
                self.helper(nums[:i]+nums[i+1:], res, path+[nums[i]])
    
if __name__ == '__main__':
    p = 4
    #q = [[1,3,4,5],[],[],[],[],[2,4]]
#    q.right.right = TreeNode(0)
    q = [1, 2, 3]
    print Solution().permute(q)   