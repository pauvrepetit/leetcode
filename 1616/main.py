
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        n = len(a)
        for i in range(n):
            if a[i] != b[n-i-1]:
                new_str = a[:i] + b[i:]
                if new_str == new_str[::-1]:
                    return True
                new_str = a[:n-i] + b[n-i:]
                if new_str == new_str[::-1]:
                    return True
                break
        for i in range(n):
            if b[i] != a[n-i-1]:
                new_str = b[:i] + a[i:]
                if new_str == new_str[::-1]:
                    return True
                new_str = b[:n-i] + a[n-i:]
                if new_str == new_str[::-1]:
                    return True
                return False
        return True

print(Solution().checkPalindromeFormation(a = "x", b = "y"))
print(Solution().checkPalindromeFormation(a = "abdef", b = "fecab"))
print(Solution().checkPalindromeFormation(a = "ulacfd", b = "jizalu"))
print(Solution().checkPalindromeFormation(a = "aejbaalflrmkswrydwdkdwdyrwskmrlfqizjezd", b = "uvebspqckawkhbrtlqwblfwzfptanhiglaabjea"))