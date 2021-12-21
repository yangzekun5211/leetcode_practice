# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:47:37 2021

@author: zyang672
"""
# Consider it in the normal devision method

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        s1 = set(s)
        l = list(s1)
        l.sort()
        res = ""
        
        while l:
            for i in range(len(l)):
                value = l[i]
                index = s.index(value)
                if set(l).issubset(set(s[index:])):
                    l.remove(value)
                    res+=value
                    s = s[index+1:]
                    break
        return res
            
    
if __name__ == '__main__':
    p = 1
    q = "abdbeca"
#    q.right.right = TreeNode(0)
    print Solution().removeDuplicateLetters( q)   