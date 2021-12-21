# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:47:37 2021

@author: zyang672
"""
# Consider it in the normal devision method
class Solution(object):
    def helper(self, nums, path, cur, i):

        cur.sort()
        if len(cur) == i:
            if cur in path:
                return 
            else:
                path.append(cur)
                return
                
        for j in range(len(nums)):
            self.helper(nums[:j]+nums[j+1:], path, cur+[nums[j]], i)
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = []
        for i in xrange(1, n+1):
            path = []
            cur = []
            self.helper(nums, path, cur, i)
            res.extend(path)
        f = 0
        
        for j in res:
            l = list(j)
            s = 0
            for k in l:
                s ^= k
            f += s
        return f
    
if __name__ == '__main__':
    p = 4
    #q = [[1,3,4,5],[],[],[],[],[2,4]]
#    q.right.right = TreeNode(0)
    q = [1,1,1]
    print Solution().subsetXORSum(q)   