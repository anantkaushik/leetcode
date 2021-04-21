"""
Problem Link: https://leetcode.com/problems/minimum-height-trees/

A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, 
any connected graph without simple cycles is a tree.
Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates 
that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. 
When you select a node x as the root, the result tree has height h. Among all possible rooted trees, 
those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).
Return a list of all MHTs' root labels. You can return the answer in any order.
The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

Example 1:
Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

Example 2:
Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]

Example 3:
Input: n = 1, edges = []
Output: [0]

Example 4:
Input: n = 2, edges = [[0,1]]
Output: [0,1]
 
Constraints:
1 <= n <= 2 * 104
edges.length == n - 1
0 <= ai, bi < n
ai != bi
All the pairs (ai, bi) are distinct.
The given input is guaranteed to be a tree and there will be no repeated edges.
"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = {}
        
        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = set()
            
            if edge[1] not in graph:
                graph[edge[1]] = set()
            
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        
        leaves = {node for node, child in graph.items() if len(child) == 1}

        # eat the leaves approach
        while n > 2:
            n -= len(leaves)
            new_leaves = set()
            for leave in leaves:
                node = graph[leave].pop()
                graph[node].remove(leave)
                if len(graph[node]) == 1:
                    new_leaves.add(node)
            leaves = new_leaves

        # atmost two roots in case of even number of nodes and one root in case of odd number od nodes
        return list(leaves)
