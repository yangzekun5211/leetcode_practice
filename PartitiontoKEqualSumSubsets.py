# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:47:37 2021

@author: zyang672
"""
class Solution(object):
    def helper(self, nums, s):
        if not nums:
            return True
        
        i = len(nums) - 1
        while i>=0 and nums[i]==s :
            i -= 1
        if i == -1:
            return True
        elif nums[0]+nums[i] != s:
            return False
        else:
            return self.helper(nums[1:i], s)
            
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if sum(nums)%k:
            return False
        
        s = sum(nums)/k
        nums.sort()
        res = self.helper(nums, s)
        return res
    
if __name__ == '__main__':
    p = 2
    #q = [[1,3,4,5],[],[],[],[],[2,4]]
#    q.right.right = TreeNode(0)
    q = [1,1,1,1,2,2,2,2]
    print Solution().canPartitionKSubsets(q, p)   