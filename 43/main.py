# 43. 字符串相乘
#
# 20210716
# huao
#

class Solution:
    def simple_multiply(self, num1: str, num2: str) -> str:
        num2 = int(num2)
        num1_len = len(num1)
        res = ""
        carry = 0
        for i in range(num1_len):
            t = int(num1[num1_len - i - 1]) * num2 + carry
            carry = t // 10
            t = t % 10
            res = str(t) + res
        if carry != 0:
            res = str(carry) + res
        return res

    def add(self, num1: str, num2: str) -> str:
        num1_len = len(num1)
        num2_len = len(num2)
        res = ""
        carry = 0
        for i in range(min(num1_len, num2_len)):
            t = int(num1[num1_len - i - 1]) + int(num2[num2_len - i - 1]) + carry
            carry = t // 10
            t = t % 10
            res = str(t) + res
        num = num1 if num1_len > num2_len else num2
        num_len = len(num)
        for i in range(min(num1_len, num2_len), max(num1_len, num2_len)):
            t = int(num[num_len - i - 1]) + carry
            carry = t // 10
            t = t % 10
            res = str(t) + res
        if carry != 0:
            res = str(carry) + res
        return res

    def multiply(self, num1: str, num2: str) -> str:
        num2_len = len(num2)
        res = "0"
        for i in range(num2_len):
            res = self.add(res, self.simple_multiply(num1, num2[num2_len - i - 1]) + "0" * i)
        while len(res) != 1 and res[0] == '0':
            res = res[1:]
        return res

# print(Solution().multiply("12345", "0"))
