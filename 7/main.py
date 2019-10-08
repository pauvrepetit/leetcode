class Solution:
    def reverse(self, x: int) -> int:
        if x <= 0:
            sign = 1
            x = -x
        else:
            sign = 0
        str_x = str(x)
        str_x = str_x[-1::-1]
        x_reverse = int(str_x)
        if sign == 1:
            x_reverse = -x_reverse
        if x_reverse < -2 ** 31 or x_reverse > (2 ** 31 - 1):
            return 0
        return x_reverse

sol = Solution()
print(sol.reverse(123))
print(sol.reverse(120))
print(sol.reverse(-123))
