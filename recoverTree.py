# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 23:12:58 2021

@author: zyang672

Basic idea: inorder tree traversal + two points
first point feature: first node that has value greater than any later nodes
second point feature: last node that has value less that the first point
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        fst = [None]
        snd = [None]
        curr = root
        stack = []
        prev = TreeNode(float('-inf'))
        if not root:
            return 

        while stack or curr:
            while curr != None:
                stack.append(curr)
                curr = curr.left
            node = stack.pop()
            if fst[0]==None and node.val < prev.val:
                fst[0] = prev
                
            if fst[0] and node.val < prev.val:
                snd[0] = node
            prev = node
            curr = node.right
            
        fst[-1].val, snd[-1].val = snd[-1].val, fst[-1].val

        
if __name__ == '__main__':
    p = TreeNode(1)
    p.right, p.left = TreeNode(3), TreeNode(2)
    q = TreeNode(1)
    q.right, q.left = TreeNode(2), TreeNode(3)
#    q.right.right = TreeNode(0)
    Solution().recoverTree(p)       
    print(p)