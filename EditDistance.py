# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 00:52:09 2021

@author: zyang672
"""

# Definition for a binary tree node.
import collections
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        dp = [[0 for i in range(m)] for j in range(n)]
        for i in range(m):
            if word1[i] in list(word2):
                dp[0][i] = i
            else:
                dp[0][i] = i + 1
        for j in range(n):
            if word1[j] in list(word2):
                dp[j][0] = j
            else:
                dp[j][0] = j + 1
        
        for j in range(1, n):
            for i in range(1, m):
                if word1[i] == word2[j]:
                    dp[j][i] = dp[j-1][i-1]
                else:    
                    dp[j][i] = min([dp[j-1][i-1], dp[j][i-1], dp[j-1][i]]) + 1
                
        return dp[n-1][m-1]
    
                    
            
            
        
if __name__ == '__main__':
    p = "sea"
    q = "eat"
    #p.right, p.left = TreeNode(2), TreeNode(3)

    #q.right, q.left = TreeNode(2), TreeNode(3)
#    q.right.right = TreeNode(0)
    print Solution().minDistance(p, q)        