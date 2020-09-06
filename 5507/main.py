# 1576. 替换所有的问号
# 周赛No.205
#
# 20200906
# huao


class Solution:
    def modifyString(self, s: str) -> str:
        s = 'a' + s + 'a'
        s = list(s)
        for i in range(len(s)):
            if s[i] == '?':
                if s[i-1] != 'a' and s[i+1] != 'a':
                    s[i] = 'a'
                elif s[i-1] != 'b' and s[i+1] != 'b':
                    s[i] = 'b'
                else:
                    s[i] = 'c'
        ss = ''
        for c in s[1:len(s)-1]:
            ss += c
        return ss
            

print(Solution().modifyString('?zs'))
print(Solution().modifyString('ubv?w'))
print(Solution().modifyString("j?qg??b"))
print(Solution().modifyString("??yw?ipkj?"))
