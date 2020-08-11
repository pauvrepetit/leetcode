# 1433. 检查一个字符串是否可以打破另一个字符串
#
# 20200811
# huao
# 排序 比较

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        length = len(s1)
        if length != len(s2):
            return False
        list1 = list(s1)
        list1.sort()
        list2 = list(s2)
        list2.sort()
        large = 0
        less = 0
        for i in range(length):
            if list1[i] > list2[i]:
                large += 1
                if less != 0:
                    return False
            elif list1[i] < list2[i]:
                less += 1
                if large != 0:
                    return False
        return True


print(Solution().checkIfCanBreak(s1="abc", s2="xya"))
