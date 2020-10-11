"""
Problem Link: https://leetcode.com/problems/number-of-islands/

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water 
and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid 
are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
class DSU:
    
    def __init__(self, n):
        self.sets = list(range(n))
        
    def find(self, index):
        if self.sets[index] != index:
            return self.find(self.sets[index])
        return index
    
    def union(self, x, y):
        self.sets[self.find(x)] = self.sets[self.find(y)]
    
    def mark_invalid(self, index):
        self.sets[index] = -1
    
    def count_unique_sets(self):
        return sum(1 for i in range(len(self.sets)) if i == self.sets[i])
    
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        self.row = len(grid)
        self.col = len(grid[0])
        dsu = DSU(len(grid) * len(grid[0]))
        
        for r in range(self.row):
            for c in range(self.col):
                pos = self.find_pos(r,c)
                
                if self.is_valid(r,c, grid):
                    if self.is_valid(r+1, c, grid):
                        dsu.union(pos, self.find_pos(r+1,c))
                    if self.is_valid(r, c+1, grid):
                        dsu.union(pos, self.find_pos(r,c+1))
                else:
                    dsu.mark_invalid(pos)
        
        return dsu.count_unique_sets()
    
    
    def find_pos(self, r, c):
        return (self.col * r) + c
    
    def is_valid(self, r, c, grid):
        return r < len(grid) and c < len(grid[0]) and grid[r][c] == "1" 



class Solution1:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        visited = [[1]*len(grid[0]) for _ in range(len(grid))]
        count = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if visited[row][col]:
                    count += grid[row][col] == "1"
                    self.dfs(grid, visited, row, col)
        return count
                    
                    
    def dfs(self, grid, visited, row, col):
        if not visited[row][col] or grid[row][col] == "0":
            return
        
        visited[row][col] = 0
        
        if col + 1 < len(grid[0]):
            self.dfs(grid, visited, row, col+1)
        if row + 1 < len(grid):
            self.dfs(grid, visited, row+1, col)
        if col - 1 >= 0:
            self.dfs(grid, visited, row, col-1)
        if row - 1 >= 0 :
            self.dfs(grid, visited, row-1, col)