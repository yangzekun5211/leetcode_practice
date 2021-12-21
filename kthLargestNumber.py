# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:47:37 2021

@author: zyang672
"""
# Consider it in the normal devision method

class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        d = {num:len(num) for num in nums}
        
        m = max(d.values())
        while k>0:
            c = 0
            for num in nums:
                if d[num] == m:
                    c += 1
            if k > c:
                k -= c
                m -= 1
            else:
                break
        
        l = []
        for num in nums:
            if d[num] == m:
                l.append(int(num))
        
        l.sort()
        return l[k-1]
            
    
if __name__ == '__main__':
    p = 1
    q = ["0", "0"]
#    q.right.right = TreeNode(0)
    print Solution().kthLargestNumber( q, 2)   