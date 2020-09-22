# 面试题 17.17. 多次搜索
#
# 20200727
# huao
# 逐个的扫、判断...


from typing import List


class Solution:
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        searchResult = []
        for small in smalls:
            searchResult.append(self.search(big, small))
        return searchResult

    def search(self, big: str, small: str) -> List[int]:
        if small == "":
            return []
        searchResult = []
        for i in range(len(big) - len(small) + 1):
            if big[i:].startswith(small):
                searchResult.append(i)
        return searchResult


sol = Solution()
print(sol.multiSearch("mississippi", [
      "is", "ppi", "hi", "sis", "i", "ssippi"]))
