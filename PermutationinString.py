# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:47:37 2021

@author: zyang672
"""

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        d_s1 = {}
        for i in s1:
            if i not in d_s1:
                d_s1[i] = 1
            else:
                d_s1[i] += 1
        d = {}
        cur = 0
        srt = 0
        while cur < len(s2):
            if s2[cur] in s1:
                if s2[srt] not in s1:
                    srt = cur
                if s2[cur] not in d:
                    d[s2[cur]] = 1
                else:
                    d[s2[cur]] += 1
                if cur-srt == len(s1)-1:
                    if d == d_s1:
                        return True
                    else:
                        d[s2[srt]] -= 1
                        srt += 1
            else:
                d = {}
                srt = cur + 1
            cur += 1
        return False
    
if __name__ == '__main__':
    p = "adc"

    q = "dcda"
#    q.right.right = TreeNode(0)
    print Solution().checkInclusion(p, q)   