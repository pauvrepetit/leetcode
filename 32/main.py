# 32. 最长有效括号
#
# 20200724
# huao
# 怎么做呢，想想编译原理里面的那些分析方法，就类似的做一下
# 我们从输入串中逐个的取字符到分析栈中
# 如果分析栈顶出现()则将其归约成数字1，如果此时1的前面还是个数字，那么我们就把这两个数字归约成两数之和
# 由于数字只能通过()归约产生，因此，只要在此归约过程中完成了数字的加法，往后就不会出现两个数字连续出现了
# 如果出现(数字)，将其归约为该数字加1
# 其他情况，就将输入符号压入分析栈中
# 分析完成后，栈中最大的数字，就是最长的有效括号串的长度

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        str = []
        strLen = 0
        for i in range(len(s)):
            if s[i] == '(':
                str.append('(')
                strLen += 1
            else:
                # s[i] == ')'
                if strLen == 0:
                    continue
                if str[strLen - 1] == '(':
                    str.pop()
                    strLen -= 1
                    if strLen != 0 and str[strLen - 1] != '(' and str[strLen - 1] != ')':
                        str[strLen - 1] += 1
                    else:
                        str.append(1)
                        strLen += 1
                elif str[strLen - 1] == ')':
                    str.append(')')
                    strLen += 1
                else:
                    # 前面是个数字
                    if str[strLen - 2] == '(':
                        str[strLen - 2] = str[strLen - 1] + 1
                        str.pop()
                        strLen -= 1
                        if strLen != 1 and str[strLen - 2] != '(' and str[strLen - 2] != ')':
                            str[strLen - 2] += str[strLen - 1]
                            str.pop()
                            strLen -= 1
                    else:
                        str.append(')')
                        strLen += 1
        maxLen = 0
        for i in str:
            if i != '(' and i != ')':
                maxLen = max(maxLen, i)
        return maxLen * 2


sol = Solution()
print(sol.longestValidParentheses(")()())()()("))
