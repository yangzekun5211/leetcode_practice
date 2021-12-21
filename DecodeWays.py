# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 00:52:09 2021

@author: zyang672
"""

# Definition for a binary tree node.
import collections
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = [1]
        if s[0] == "0":
            return 0
        else:
            result.append(1)
            
        for i in range(1, len(s)):
            cur = 0
            if 0 < int(s[i]) and 10 > int(s[i]):
                cur += result[i]
            if 9 < int(s[i-1:i+1]) and 26 > int(s[i-1:i+1]):
                cur += result[i-1]
            result.append(cur)
        return result[-1]
    
                    
            
            
        
if __name__ == '__main__':
    p = "sea"
    q = "eat"
    #p.right, p.left = TreeNode(2), TreeNode(3)

    #q.right, q.left = TreeNode(2), TreeNode(3)
#    q.right.right = TreeNode(0)
    print Solution().numDecodings('2')        