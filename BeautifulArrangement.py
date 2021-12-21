# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:47:37 2021

@author: zyang672
"""
class Solution(object):
    def bk_helper(self, remain, path):
        if not self.beautiful_helper(path):
            return 
        
        if not remain:
            if self.beautiful_helper(path):
                self.res += 1
            return 
            
        for i in range(len(remain)):
            self.bk_helper(remain[:i]+remain[i+1:], path+[remain[i]])
            
            
    def beautiful_helper(self, nums):
        for i in xrange(len(nums)):
            if nums[i]%(i+1) and (i+1)%nums[i]:
                return False
        return True
    
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res = 0
        nums = [i for i in xrange(1, n+1)]
        self.bk_helper(nums, [])
        return self.res
    
if __name__ == '__main__':
    p = 4
    #q = [[1,3,4,5],[],[],[],[],[2,4]]
#    q.right.right = TreeNode(0)
    q = [1,1,1]
    print Solution().countArrangement(11)   