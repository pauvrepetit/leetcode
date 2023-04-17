#
# @lc app=leetcode.cn id=793 lang=python3
#
# [793] 阶乘函数后 K 个零
#

# @lc code=start
class Solution:
    def cal(self, n: int, m: int) -> int:
        # n是一个数，比如说10
        # m是一个数，只能是2或者5，比如说2
        # 返回，1-n这n个数中因子2的个数
        if n <= 0:
            return 0
        count = 0
        while n // m != 0:
            count += n // m
            n = n // m
        return count

    def preimageSizeFZF(self, k: int) -> int:
        # 用二分法找大致的k对于2/5的大致的n
        # 先算5的情况
        begin = 0
        end = (k + 1) * 5
        mid = (begin + end) // 2
        while begin != mid:
            count = self.cal(mid, 5)
            if count == k:
                # return 5
                # 现在count5[mid]==k了，他附近的count5也可能是k，我们小搜索一下
                for i in range(mid-5, mid+6):
                    if self.cal(i, 5) == k and self.cal(i, 2) >= k:
                        return 5
                return 0
            if count > k:
                end = mid
            else:
                begin = mid
            mid = (begin + end) // 2

        begin = 0
        end = (k + 1) * 2
        mid = (begin + end) // 2
        while begin != mid:
            count = self.cal(mid, 2)
            if count == k:
                for i in range(mid-2, mid+3):
                    if self.cal(i, 2) == k and self.cal(i, 5) >= k:
                        return 2
                return 0
            if count > k:
                end = mid
            else:
                begin = mid
            mid = (begin + end) // 2
        return 0

# @lc code=end

print(Solution().preimageSizeFZF(0))
print(Solution().preimageSizeFZF(3))
print(Solution().preimageSizeFZF(5))
print(Solution().preimageSizeFZF(80502705))
print(Solution().preimageSizeFZF(79))

# 唉，这个题好久之前就做过一次，但是没过了，又搞了好几天
