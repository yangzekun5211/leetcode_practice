# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 00:52:09 2021

@author: zyang672
"""

# Definition for a binary tree node.
from copy import deepcopy
class Solution(object):
    def helper(self, flag, rest, i, j):
        if not rest:
            return True
        
        directs = [[0,1], [0,-1], [1,0], [-1,0]]
        for d in directs:
            cur = deepcopy(flag)
            x = i + d[0]
            y = j + d[1]
            if x >= 0 and x < self.m and y >= 0 and y < self.n and not cur[x][y] and self.board[x][y] == rest[0]:
                cur[x][y] = 1
                if self.helper(cur, rest[1:], x, y):
                    return True
                    
        return False
        
        
    def exist(self, board, word, i, j):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.board = board
        self.m = len(word)
        self.n = len(word[0])
        flag = [[0 for i in range(self.n)] for j in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] == word[0]:
                    flag[i][j] = 1;
                    if self.helper(flag, word[1:], i, j):
                        return True
        return False
                
    
if __name__ == '__main__':
    p = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    q = word = "ABCCED"

#    q.right.right = TreeNode(0)
    print Solution().exist(q)         