# 881. 救生艇
#
# 20200725
# huao
# 因为有一个救生艇最多两个人的限制，所有这样想应该是没问题的
# 从大到小排序
# 找最重的那个人，给他找一个救生艇可以承受的同伴一组
# 重复上述操作即可
# 因为排过序，所有可以二分查找，不然会超时

from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        i = 0
        count = 0
        while i < len(people):
            j = self.binarySearch(
                people, limit - people[i], i + 1, len(people))
            if j >= 0:
                people.pop(j)
            count += 1
            i += 1
        return count

    def binarySearch(self, people: List[int], target: int, begin: int, end: int) -> int:
        if begin == end:
            return -1
        if begin + 1 == end:
            if people[begin] <= target:
                return begin
            elif end != len(people) and people[end] <= target:
                return end
            else:
                return -1

        mid = (begin + end) // 2
        if people[mid] == target:
            return mid
        elif people[mid] > target:
            return self.binarySearch(people, target, mid, end)
        else:
            return self.binarySearch(people, target, begin, mid)


sol = Solution()
print(sol.numRescueBoats([1, 2, 2, 3], 3))
print(sol.numRescueBoats([3, 5, 3, 4], 5))
print(sol.numRescueBoats([44, 10, 29, 12, 49, 41, 23, 5, 17, 26], 50))
