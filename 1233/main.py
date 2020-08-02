# 1233. 删除子文件夹
#
# 20200802
# huao
# 排序 判断

from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        i = 0
        while i < len(folder):
            while i + 1 != len(folder) and self.isSubStr(folder[i], folder[i+1]):
                folder.pop(i + 1)
            i += 1
        return folder

    def isSubStr(self, x: str, y: str) -> bool:
        lenx = len(x)
        leny = len(y)
        if lenx >= leny:
            return False
        if y.startswith(x) and y[lenx] == '/':
            return True
        return False


sol = Solution()
print(sol.removeSubfolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]))
