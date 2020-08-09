# 696. 计数二进制子串
#
# 20200809
# huao
# 不要动不动就O(n^2)

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = []
        while s != "":
            loc = self.countNum(s, s[0])
            s = s[loc:]
            count.append(loc)
        subCount = 0
        for i in range(1, len(count)):
            subCount += min(count[i-1], count[i])
        return subCount

    def countNum(self, s: str, n: str) -> int:
        count = 0
        for c in s:
            if c == n:
                count += 1
            else:
                break
        return count


sol = Solution()
print(sol.countBinarySubstrings("00110011"))
print(sol.countBinarySubstrings("10101"))
