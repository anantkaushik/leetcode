"""
Problem Link: https://leetcode.com/problems/rotting-oranges/

You are given an m x n grid where each cell can have one of three values:
0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        fresh_oranges = mins = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append([row, col])
                elif grid[row][col] == 1:
                    fresh_oranges += 1
        
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while queue and fresh_oranges:
            l = len(queue)
            mins += 1
            
            for _ in range(l):
                row, col = queue.pop(0)

                for r, c in directions:
                    new_row = row + r
                    new_col = col + c

                    if new_row < 0 or new_col < 0 or new_col >= len(grid[0]) or new_row >= len(grid) or grid[new_row][new_col] in [0, 2]:
                        continue

                    queue.append([new_row, new_col])
                    grid[new_row][new_col] = 2
                    fresh_oranges -= 1
            
            
        
        return mins if fresh_oranges == 0 else -1


class Solution1:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = [[-1] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    self.dfs(grid, time, i+1, j, 1)
                    self.dfs(grid, time, i, j+1, 1)
                    self.dfs(grid, time, i-1, j, 1)
                    self.dfs(grid, time, i, j-1, 1)

        
        return self.find_time(grid, time)
        
    
        
    def dfs(self, grid, time, i, j, time_taken):
        if not self.isvalid(grid, i, j):
            return 

        if (grid[i][j] == 1) and (time[i][j] == -1 or time_taken < time[i][j]):
            time[i][j] = time_taken

            self.dfs(grid, time, i+1, j, time_taken+1)
            self.dfs(grid, time, i, j+1, time_taken+1)
            self.dfs(grid, time, i-1, j, time_taken+1)
            self.dfs(grid, time, i, j-1, time_taken+1)
        
    
    def isvalid(self, grid, i, j):
        if i < 0 or j < 0 or j >= len(grid[0]) or i >= len(grid):
            return False
        return True
    
    def find_time(self, grid, time):
        max_time = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and time[i][j] == -1:
                    return -1
                max_time = max(max_time, time[i][j])
        
        return max_time
