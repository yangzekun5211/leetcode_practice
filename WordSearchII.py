# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 00:52:09 2021

@author: zyang672
"""

# Definition for a binary tree node.
import copy

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        def findWord(board, word, r, c):
            if not word:
                return True
            
            res = False
            #print(r)
            #print(c)
            if board[r][c] == word[0]:
                if len(word) == 1:
                    return True
                new_board = copy.deepcopy(board)
                new_board[r][c] = "A"
                if r > 0:
                    res = res or findWord(new_board, word[1:], r-1, c)
                    if res:
                        return True
                if r < len(board)-1:
                    res = res or findWord(new_board, word[1:], r+1, c)
                    if res:
                        return True
                if c > 0:
                    res = res or findWord(new_board, word[1:], r, c-1)
                    if res:
                        return True
                if c < len(board[0])-1:
                    res = res or findWord(new_board, word[1:], r, c+1)
                    if res:
                        return True
                return False
            
        m = len(board)
        n = len(board[0])
        res = []
        for i in range(m):
            for j in range(n):
                k = 0
                while k < len(words):
                    word = words[k]
                    if findWord(board, word, i, j):
                        res.append(word)
                        words.remove(word)
                    else:
                        k += 1
        return res
            
        
if __name__ == '__main__':
    p = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    p = [["a"]]
    #p.right, p.left = TreeNode(2), TreeNode(3)
    q = ["oath","pea","eat","rain"]
    q = ["a"]
    #q.right, q.left = TreeNode(2), TreeNode(3)
#    q.right.right = TreeNode(0)
    print Solution().findWords(p, q)         