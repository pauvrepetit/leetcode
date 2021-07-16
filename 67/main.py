# 67. 二进制求和
#
# 20210716
# huao


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        alen = len(a)
        blen = len(b)
        res = ""
        carry = 0
        for i in range(min(alen, blen)):
            t = int(a[alen - i - 1]) + int(b[blen - i - 1]) + carry
            carry = t // 2
            t = t % 2
            res = str(t) + res
        num = a if alen > blen else b
        numlen = len(num)
        for i in range(min(alen, blen), max(alen, blen)):
            t = int(num[numlen - i - 1]) + carry
            carry = t // 2
            t = t % 2
            res = str(t) + res
        if carry != 0:
            res = str(carry) + res
        return res


print(Solution().addBinary("11", "1"))
print(Solution().addBinary("1010", "1011"))
