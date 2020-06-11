#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] unique-binary-search-trees-ii
#
import functools
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0: return []
        # 加速缓存
        @functools.lru_cache(None)
        def helper(start, end):
            res = []
            if start > end: res.append(None)
            for val in range(start, end + 1):
                # 左子树均小于val
                for left in helper(start, val - 1):
                    # 右子树均大于val
                    for right in helper(val + 1, end):
                        # 构建树节点
                        root = TreeNode(val,left,right)
                        # root.left = left
                        # root.right = right
                        res.append(root)
            return res

        return helper(1, n)


# @lc code=end