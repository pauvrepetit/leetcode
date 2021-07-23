# 125. 验证回文串
#
# 20210719
# huao

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_char = "abcdefghijklmnopqrstuvwxyz"
        upper_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        nums = "0123456789"
        ss = ""
        for c in s:
            if c in nums or c in lower_char:
                ss += c
            if c in upper_char:
                ss += lower_char[upper_char.index(c)]
        return ss == ss[::-1]
