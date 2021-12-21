# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:47:37 2021

@author: zyang672
"""
# Consider it in the normal devision method

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        flag = 1
        if numerator*denominator < 0:
            numerator = abs(numerator)
            denominator = abs(denominator)
            flag = -1
            
        quoitent = numerator/denominator
        residue = numerator - denominator*quoitent
        if not residue:
            result = str(flag*quoitent)
            return result
        else:
            result = str(quoitent) + "."
        prefix = len(result)
        residues = []
                
        while residue and residue not in residues:
            residues.append(residue)
            numerator = 10*residue
            quoitent = numerator/denominator
            residue = numerator - denominator*quoitent
            result += str(quoitent)

        
        if not residue:
            if flag == -1:
                result = "-" + result
            return result
        else:
            index = residues.index(residue)
            result = result[:prefix+index] + "(" + result[prefix+index:] + ")"
            if flag == -1:
                result = "-" + result
            return result
            
    
if __name__ == '__main__':
    p = 1
    q = 2
#    q.right.right = TreeNode(0)
    print Solution().fractionToDecimal(p, q)   