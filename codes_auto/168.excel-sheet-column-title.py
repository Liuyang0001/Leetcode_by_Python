#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] excel-sheet-column-title
#
class Solution:
    def convertToTitle(self, n: int) -> str:
        a, b = divmod(n-1, 26)
        res = ""
        while a >= 0:
            res = chr(b + 65) + res
            a, b = divmod(a-1, 26)
        return res
# @lc code=end