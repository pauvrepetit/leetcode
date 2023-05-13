#
# @lc app=leetcode.cn id=2014 lang=python3
#
# [2014] 重复 K 次的最长子序列
#

# @lc code=start
class Solution:
    def match(self, s: str, pattern: str, k: int) -> bool:
        total_pattern = pattern * k
        i = 0
        for c in total_pattern:
            while i < len(s) and c != s[i]:
                i += 1
            if i == len(s):
                return False
            i += 1
        return True        

    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        char_dict = dict()
        chars_list = []
        for c in s:
            if c in char_dict.keys():
                char_dict[c] += 1
            else:
                char_dict[c] = 1
        for c in char_dict.keys():
            if char_dict[c] >= k:
                chars_list.append(c)
        chars_list.sort(reverse=True)
        chars = ""
        for c in chars_list:
            chars += c

        length = 0
        for c in s:
            if c in chars:
                length += 1
        # pattern中只可能有chars中的字符
        # pattern最长只能有length // k的长度
        # 遍历所有可能的pattern？
        max_length = 0
        max_pattern = ""
        index = 0
        while index < len(chars) ** (length // k):
            pattern = ""
            tmp = index
            for _ in range(length // k):
                c = chars[tmp % len(chars)]
                pattern = c + pattern
                tmp //= len(chars)
            
            for i in range(max_length, len(pattern)):
                sub_pattern = pattern[:i+1]
                matched = True
                for j in sub_pattern:
                    if sub_pattern.count(j) * k > char_dict[j]:
                        # 肯定匹配不上
                        matched = False
                if matched == True and self.match(s, sub_pattern, k):
                    max_pattern = sub_pattern
                    max_length = len(sub_pattern)
                else:
                    # sub_pattern匹配不上，那么后面都不用尝试匹配了
                    tmp = len(chars) ** (length // k - len(sub_pattern))
                    if tmp != 0:
                        index += tmp
                        index = index // tmp * tmp
                    index -= 1
                    break
            index += 1
            if max_length == len(pattern):
                return max_pattern
        return max_pattern

# @lc code=end

print(Solution().longestSubsequenceRepeatedK("uajyihjuajyijuajyij", 3))
print(Solution().longestSubsequenceRepeatedK("twhaatwhaattwhadatwhcaa", 4))
print(Solution().longestSubsequenceRepeatedK("letsleetcode", 2))
print(Solution().longestSubsequenceRepeatedK("bb", 2))
print(Solution().longestSubsequenceRepeatedK("tsrkimbtsrkimbtsrkimbtsrkimbtsrkimbtsrkimbtsrkimbtsrkimbtsrkimbtsrkimbtsrkimbtsrkimbtsrkimbtsrkimbtsrkimbtsrkimbtsrkimbtsrkimbtsrkimbtsrkimbtsrkimbtsrkimbtsrkimbtsrkimbtsrkimbtsrkimbtsrkimb", 27))
print(Solution().longestSubsequenceRepeatedK("dynytqpdynytqpdynytqpdynytqpdynytqpdynytqpdynytqpdynytqpdynytqpdynytqpdynytqpdynytqpdynytqpdynytqpdynytqpdynytqpdynytqpdynytqpdynytqpdynytqpdynytqpdynytqpdynytqpdynytqpdynytqpdynytqpdynytqpdynytqpdynytqpdynytqpdynytqpdynytqpdynytqp", 33))
print(Solution().longestSubsequenceRepeatedK("jzuaqjfjzuaqjfjzuaqjfjzuaqjfjzuaqjfjzuaqjfjzuaqjfjzuaqjfjzuaqjfjzuaqjfjzuaqjfjzuaqjfjzuaqjfjzuaqjfjzuaqjfjzuaqjfjzuaqjfjzuaqjfjzuaqjfjzuaqjfjzuaqjfjzuaqjfjzuaqjfjzuaqjfjzuaqjfjzuaqjfjzuaqjfjzuaqjfjzuaqjfjzuaqjfjzuaqjf", 31))