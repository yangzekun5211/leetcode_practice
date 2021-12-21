# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 00:52:09 2021

@author: zyang672
"""

# Definition for a binary tree node.

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        stack = []
        non_zeros = []
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    stack.append([i, j])
                else:
                    non_zeros.append([i, j])
        
        while stack:
            [i, j] = stack.pop()
            search_list = [[i, j+1], [i, j-1], [i+1, j], [i-1, j]]
            for [s, t] in search_list:
                if [s, t] in non_zeros:
                    index = non_zeros.index([s, t])
                    non_zeros.pop(index)
                    stack.append([s, t])
                    matrix[s][t] = 0
                
    
if __name__ == '__main__':
    p = -1
    q = [[1,1,1],[1,0,1],[1,1,1]]

#    q.right.right = TreeNode(0)
    print Solution().setZeroes(q)         