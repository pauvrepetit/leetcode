# 面试题 01.03. URL化
#
# 20200907
# huao

class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        return S[:length].replace(' ', '%20')


print(Solution().replaceSpaces("Mr John Smith    ", 13))
print(Solution().replaceSpaces("               ", 5))
