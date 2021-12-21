# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:47:37 2021

@author: zyang672
"""
# According to Python wiki, set in python is realized by hash table, so the complexity
# of search in a set is O(1)

from collections import Counter
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        fst = 0
        snd = k+1
        result = k
        if len(s) == k:
            return k
        
        c = Counter(s[fst:snd])
        
        while snd<=len(s):
            max_c = max(c.values())
            if max_c+k>=snd-fst:
                result = max(result, snd-fst)
                
                if snd<len(s):
                    if s[snd] in c:
                        c[s[snd]] += 1
                    else:
                        c[s[snd]] = 1
                elif snd==len(s):
                    if s[-1] in c:
                        c[s[-1]] += 1
                    else:
                        c[s[-1]] = 1
                snd += 1
            else:
                if snd-fst>result:
                    c[s[fst]] -= 1
                    fst += 1                    
                else:
                    
                    if snd<len(s):
                        if s[snd] in c:
                            c[s[snd]] += 1
                        else:
                            c[s[snd]] = 1
                    elif snd==len(s):
                        if s[-1] in c:
                            c[s[-1]] += 1
                        else:
                            c[s[-1]] = 1
                    snd += 1
        return result
    
if __name__ == '__main__':
    p = "AAAA"
    q = 0
#    q.right.right = TreeNode(0)
    print Solution().characterReplacement(p, q)   