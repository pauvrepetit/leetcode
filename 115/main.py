# 115. 不同的子序列
#
# 20200802
# huao
# 以"babgbag" 和 "bag"为例
# 我们从后向前扫描"babgbag"字符串，记录当前的"g" "ag" "bag"子序列出现的次数
# 当遇到一个g时，"g"加1
# 当遇到一个a时，"ag"加上"g"的数量
# 当遇到一个b时，"bag"加上"ag"的数量
# 当待搜索的子序列中存在相同字符时，也是适用的

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        count = [0 for i in range(len(t))]
        for c in s[::-1]:
            for i in range(len(t)):
                if c == t[i] and i == len(t) - 1:
                    count[i] += 1
                elif c == t[i]:
                    count[i] += count[i+1]
        return count[0]



sol = Solution()
print(sol.numDistinct("rabbbit", "rabbit"))
print(sol.numDistinct("babgbag", "bag"))
print(sol.numDistinct("daacaedaceacabbaabdccdaaeaebacddadcaeaacadbceaecddecdeedcebcdacdaebccdeebcbdeaccabcecbeeaadbccbaeccbbdaeadecabbbedceaddcdeabbcdaeadcddedddcececbeeabcbecaeadddeddccbdbcdcbceabcacddbbcedebbcaccac", "ceadbaa"))
