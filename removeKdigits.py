# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:47:37 2021

@author: zyang672
"""
# According to Python wiki, set in python is realized by hash table, so the complexity
# of search in a set is O(1)

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        l = len(num)-k
        srt = 0
        end = k+1
        res = ""
        while l>0:
            keep = min([int(num[i]) for i in range(srt,end)])
            srt += num[srt:end].find(str(keep)) + 1
            end += 1
            res += str(keep)
            l -= 1
        return str(int(res))
    
if __name__ == '__main__':
    p = "1432219"
    q = 3
#    q.right.right = TreeNode(0)
    print Solution().removeKdigits(p, q)   