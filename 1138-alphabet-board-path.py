"""
Problem Link: https://leetcode.com/problems/alphabet-board-path/

On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].
Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.

We may make the following moves:
'U' moves our position up one row, if the position exists on the board;
'D' moves our position down one row, if the position exists on the board;
'L' moves our position left one column, if the position exists on the board;
'R' moves our position right one column, if the position exists on the board;
'!' adds the character board[r][c] at our current position (r, c) to the answer.
(Here, the only positions that exist on the board are positions with letters on them.)
Return a sequence of moves that makes our answer equal to target in the minimum number of moves. 
You may return any path that does so.

Example 1:
Input: target = "leet"
Output: "DDR!UURRR!!DDD!"

Example 2:
Input: target = "code"
Output: "RR!DDRR!UUL!R!"
 
Constraints:
1 <= target.length <= 100
target consists only of English lowercase letters.
"""
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        pos = self.get_alphabets_pos()
        cur_pos = [0, 0]
        ans = []
        for char in target:
            target_pos = pos[char]
            if target_pos[1] < cur_pos[1]:
                ans.extend(["L"] * (cur_pos[1] - target_pos[1]))
            if target_pos[0] < cur_pos[0]:
                ans.extend(["U"] * (cur_pos[0] - target_pos[0]))
            if target_pos[0] > cur_pos[0]:
                ans.extend(["D"] * (target_pos[0] - cur_pos[0]))
            if target_pos[1] > cur_pos[1]:
                ans.extend(["R"] * (target_pos[1] - cur_pos[1]))
            ans.append("!")
            cur_pos = target_pos
            
        return "".join(ans)
        
    
    def get_alphabets_pos(self):
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        pos = {}
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                pos[board[i][j]] = [i, j]
        
        return pos


class Solution1:
    def alphabetBoardPath(self, target: str) -> str:
        pos = self.get_alphabets_pos()
        cur_pos = [0, 0]
        ans = []
        for char in target:
            target_pos = pos[char]
            
            while target_pos != cur_pos:
                if target_pos[1] < cur_pos[1]:
                    ans.append("L")
                    cur_pos[1] -= 1
                elif target_pos[0] < cur_pos[0]:
                    ans.append("U")
                    cur_pos[0] -= 1
                elif target_pos[0] > cur_pos[0]:
                    ans.append("D")
                    cur_pos[0] += 1
                elif target_pos[1] > cur_pos[1]:
                    ans.append("R")
                    cur_pos[1] += 1
            
            ans.append("!")
        
        return "".join(ans)
        
    
    def get_alphabets_pos(self):
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        pos = {}
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                pos[board[i][j]] = [i, j]
        
        return pos
