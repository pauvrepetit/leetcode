class Solution:
    def countDigitOne(self, n: int) -> int:
        # 预先算出每一位上的数字会产生多少个1
        # 一位数有多少个1 0-9
        # 两位数有多少个1 0-99
        # ...
        count = [0, 1]
        for i in range(2, 12):
            count.append(count[i-1] * 10 + 10 ** (i - 1))
        s = str(n)[::-1]
        all_count = 1
        if s[0] == '0':
            all_count = 0
        for i in range(1, len(s)):
            if s[i] == '1':
                all_count += int(s[i]) * count[i] + (int(s[:i][::-1])) + 1
            elif s[i] != '0':
                all_count += int(s[i]) * count[i] + 10 ** i
        return all_count

# for i in range(20):
#     print(Solution().countDigitOne(i))

print(Solution().countDigitOne(123))