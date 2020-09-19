# 233. 数字 1 的个数
#
# 20200919
# huao

class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n < 10:
            return 1
        count = 0
        strn = str(n)
        for i in range(len(strn)):
            before = strn[:i]
            after = strn[i+1:]
            if strn[i] == '0':
                count += int(before) * (10 ** len(after))
            elif strn[i] == '1':
                count += int(before+after) + 1
            else:
                num = 1
                if before != "":
                    num = int(before)+1
                count += num * (10 ** len(after))
        return count


print(Solution().countDigitOne(100))
