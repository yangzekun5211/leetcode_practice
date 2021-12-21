# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:47:37 2021

@author: zyang672
"""
# Consider it in the normal devision method
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        in_nodes = {}
        out_degree = {}
        queue = []
        res = []
        for i in range(len(graph)):
            if not graph[i]:
                queue.append(i)
                res.remove(i)
            else:
                out_degree[i] = len(graph[i])
                for j in graph[i]:
                    if j in in_nodes:
                        in_nodes[j].append(i)
                    else:
                        in_nodes[j] = [i]
        while queue:
            item = queue.pop(0)
            res.append[item]
            if item in in_nodes:
                for node in in_nodes[item]:
                    out_degree[node] -= 1
                    if out_degree[node] == 0:
                        queue.append(node)
                        
        return res
    
if __name__ == '__main__':
    p = 4
    #q = [[1,3,4,5],[],[],[],[],[2,4]]
#    q.right.right = TreeNode(0)
    q = [[1,2],[2,3],[5],[0],[5],[],[]]
    print Solution().eventualSafeNodes(q)   