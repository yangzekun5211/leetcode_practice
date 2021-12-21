# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:47:37 2021

@author: zyang672
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, j = 0, 1
        global_max = 0
        if not s:
            return 0
        while i<len(s) and j<=len(s):
            if len(set(s[i:j])) == j-i:
                global_max = max(global_max, j-i)
                j += 1
            else:
                i += 1
                
        return global_max
    
if __name__ == '__main__':
    p = " "
#    q.right.right = TreeNode(0)
    print Solution().lengthOfLongestSubstring(p)   