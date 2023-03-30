class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            # an email address
            name, domain = s.split('@')
            name = name.lower()
            name = name[0] + '*****' + name[-1]
            domain = domain.lower()
            return name + '@' + domain
        else:
            num = ''
            for i in s:
                if i not in '+-() ':
                    num += i
            if len(num) == 10:
                return '***-***-' + num[-4:]
            return '+' + '*' * (len(num) - 10) + '-***-***-' + num[-4:]

print(Solution().maskPII(s = "LeetCode@LeetCode.com"))
print(Solution().maskPII(s = "AB@qq.com"))
print(Solution().maskPII(s = "1(234)567-890"))
print(Solution().maskPII(s = "111(234)567-890"))
