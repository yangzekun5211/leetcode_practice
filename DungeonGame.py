# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 00:52:09 2021

@author: zyang672
"""

# Definition for a binary tree node.
class Solution:
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float("inf")]*(n+1) for _ in range(m+1)]
        dp[m-1][n], dp[m][n-1] = 1, 1
            
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j] = max(min(dp[i+1][j],dp[i][j+1])-dungeon[i][j],1)
        
        return dp[0][0]
            
        
if __name__ == '__main__':
    #p = TreeNode(1)
    #p.right, p.left = TreeNode(2), TreeNode(3)
    q = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
    #q.right, q.left = TreeNode(2), TreeNode(3)
#    q.right.right = TreeNode(0)
    print Solution().calculateMinimumHP(q)         