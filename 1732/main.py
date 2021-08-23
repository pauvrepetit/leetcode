# 1732. 找到最高海拔
#
# 20210823
# huao

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        height = 0
        max_height = 0
        for diff in gain:
            height += diff
            max_height = max(max_height, height)
        return max_height
