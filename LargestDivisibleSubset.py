# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:47:37 2021

@author: zyang672
"""
class Solution(object):

    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        n_path = {}
        nums.sort()
        for i in range(len(nums)):
            if not i:
                n_path[nums[i]] = [nums[i]]
                continue
            flag = 0
            pathes = []
            for n in n_path.keys():
                if not nums[i]%n:
                    pathes.append(n_path[n]+[nums[i]])
                    flag = 1
            if not flag:
                pathes.append([nums[i]])
            length = [len(p) for p in pathes]
            max_value = max(length)
            max_index = length.index(max_value)
            n_path[nums[i]] = pathes[max_index]
            
        pathes = n_path.values()
        length = [len(p) for p in pathes]
        max_value = max(length)
        max_index = length.index(max_value)
        return pathes[max_index]
    
if __name__ == '__main__':
    p = 4
    #q = [[1,3,4,5],[],[],[],[],[2,4]]
#    q.right.right = TreeNode(0)
    q = [5,9,18,54,108,540,90,180,360,720]
    print Solution().largestDivisibleSubset(q)   