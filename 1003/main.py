# 1003. 检查替换后的词是否有效
#
# 20200801
# huao
# python处理字符串就是舒适

class Solution:
    def isValid(self, S: str) -> bool:
        while S != "":
            if "abc" in S:
                S = S.replace("abc", "")
            else:
                return False
        return True


sol = Solution()
print(sol.isValid("cababc"))
