from typing import List

class Solution:
    def permutation(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        if len(s) == 1:
            return [s]
        res = set()
        for i in range(len(s)):
            c = s[i]
            next_res = self.permutation(s[:i] + s[i+1:])
            for j in range(len(next_res)):
                res.add(next_res[j] + c)
        return list(res)
