class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        str_x = str(x)
        str_re_x = str_x[-1::-1]
        if str_x == str_re_x:
            return True
        return False

sol = Solution()
print(sol.isPalindrome(121))
print(sol.isPalindrome(10))
print(sol.isPalindrome(-121))
