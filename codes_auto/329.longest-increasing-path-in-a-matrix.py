#
# @lc app=leetcode.cn id=329 lang=python3
#
# [329] longest-increasing-path-in-a-matrix
#
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]: return 0
        row, col = len(matrix), len(matrix[0])
        move = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        
        @functools.lru_cache(None)
        def helper(x, y):
            # visit[x][y] = 1
            res = 0
            for x_off, y_off in move:
                i, j = x + x_off, y + y_off
                if 0 <= i < row and 0 <= j < col \
                        and matrix[i][j] > matrix[x][y]:
                    res = max(res,helper(i, j)) 
            return res + 1
        
        res = 0           
        for i in range(row):
            for j in range(col):
                # 路径是严格单调增的
                # visit = [[0] * col for _ in range(row)]
                res = max(res, helper(i, j))
        return res
            
# @lc code=end