# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:47:37 2021

@author: zyang672
"""
# Consider it in the normal devision method

class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        def fraction(num):
            vals = num.split('/')
            res = float(int(vals[0]))/float(int(vals[1]))
            return res
        
        nums1 = expression.split('+')
        res = 0
        for nums2 in nums1:
            if '-' not in nums2:
                res += fraction(nums2)
            else:
                num = nums2.split('-')
                if num[0]:
                    res += fraction(num[0])
                for i in range(1,len(num)):
                    res -= fraction(num[i])
        i = 1
        if res > -0.0001:
            flag = ''
        else:
            res = abs(res)
            flag = '-'
        while i:
            j = 1
            while j:
                v = (j*res+0.001)%i
                if v < 0.01:
                    return flag+str(int(j*res))+'/'+str(j)
                j += 1
            i += 1
            
    
if __name__ == '__main__':
    p = 1
    q ="7/2+2/3-3/4"
#    q.right.right = TreeNode(0)
    print Solution().fractionAddition( q)   