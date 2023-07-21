#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        if s == "":
            return s
        if s[0] in '123456789':
            begin = -1
            end = 0
            begin_count = 0
            end_count = 0
            for i in range(len(s)):
                if s[i] == '[':
                    if begin == -1:
                        begin = i+1
                    begin_count += 1
                if s[i] == ']':
                    end = i
                    end_count += 1
                    if begin_count == end_count:
                        return int(s[:begin-1]) * self.decodeString(s[begin:end]) + self.decodeString(s[end+1:])
        for i in range(len(s)):
            if s[i] in '123456789':
                return s[:i] + self.decodeString(s[i:])
        return s

# @lc code=end

print(Solution().decodeString("3[a2[c]]"))