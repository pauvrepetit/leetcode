# 面试题 16.11. 跳水板
#
# 20200801
# huao
# 这个看似复杂，实际上很简单的
# 首先全部取短的那种
# 接下来就是逐个换成长的那种
# 反正就两种板子 一个等差数列就好了

class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []
        if longer == shorter:
            return [i for i in range(shorter*k, longer*k+1)]
        return [i for i in range(shorter*k, longer*k+1)[::(longer-shorter)]]
