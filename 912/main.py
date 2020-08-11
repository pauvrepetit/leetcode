# 912. 排序数组
#
# 20200811
# huao
# 你说排序是吧 调库函数自然最舒适的 而且比我自己写的还快
# 要真让我写个排序算法 O(n^2)的还好 O(nlogn)的我大概还只会写归并...

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)
