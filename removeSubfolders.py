# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:47:37 2021

@author: zyang672
"""
# Consider it in the normal devision method

from collections import OrderedDict
class Solution(object):
    
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        dd = {}
        for f in folder:
            dd[f] = len(f)
        od = OrderedDict(sorted(dd.items(),key=lambda t:t[1]))
        res = []
        for f in od.keys():
            res.append(f)
            for i in res[:-1]:
                if f[:od[i]] == i and f[od[i]] == '/':
                    res.pop()
                    break
            
        return res
            
    
if __name__ == '__main__':
    p = 1
    q = ["/ah/al/am","/ah/al"]
#    q.right.right = TreeNode(0)
    print Solution().removeSubfolders( q)   