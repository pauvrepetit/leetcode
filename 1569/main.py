# 1569. 将子数组重新排序得到同一个二叉查找树的方案数
# 周赛No.204
# 
# 20200905
# huao

from typing import List


# def comb(n, k):
#     if k == 1:
#         return n
#     if k == 0:
#         return 1
#     return comb(n, k-1) * (n-k+1) // k

yanghui = [[0 for i in range(1002)] for j in range(1002)]


def comb(n, k):
    if yanghui[n][k] == 0:
        yanghui[n][k] = (comb(n-1, k-1) + comb(n-1, k)) % 1000000007
    return yanghui[n][k]


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        for i in range(1002):
            yanghui[i][0] = 1
            yanghui[i][i] = 1
        return (self.cal(nums) - 1) % 1000000007

    def cal(self, nums: List[int]) -> int:
        if nums == []:
            return 1
        root = nums[0]
        left = []
        right = []
        for num in nums:
            if num < root:
                left.append(num)
            elif num > root:
                right.append(num)
        return comb(len(nums)-1, len(left)) * self.cal(left) * self.cal(right) % 1000000007


print(Solution().numOfWays(
    nums=[9, 4, 2, 1, 3, 6, 5, 7, 8, 14, 11, 10, 12, 13, 16, 15, 17, 18]))
print(Solution().numOfWays([3, 1, 2, 5, 4, 6]))

print(Solution().numOfWays([3, 4, 5, 1, 2]))
