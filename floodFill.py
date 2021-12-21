# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:47:37 2021

@author: zyang672
"""

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r+1 < R: dfs(r+1, c)
                if r >= 1: dfs(r-1, c)
                
                if c >= 1: dfs(r, c-1)
                if c+1 < C: dfs(r, c+1)

        dfs(sr, sc)
        return image
    
if __name__ == '__main__':
    image = [[1,1,1],[1,1,0],[1,0,1]]
    p = 1

    q = 1
    c = 2
#    q.right.right = TreeNode(0)
    print Solution().floodFill(image, p, q, c)   