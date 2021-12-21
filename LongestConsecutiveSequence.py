# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:47:37 2021

@author: zyang672
"""
# According to Python wiki, set in python is realized by hash table, so the complexity
# of search in a set is O(1)

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: list
        :rtype: int
        """
        nums = set(nums)
        global_max = 0
        for i in nums:
            if i-1 not in nums:
                local = 1
                j = i+1
                while j in nums:
                    j += 1
                    local += 1
                global_max = max(local, global_max)
                
        return global_max
    
if __name__ == '__main__':
    p = [100,4,200,1,3,2]
#    q.right.right = TreeNode(0)
    print Solution().longestConsecutive(p)   