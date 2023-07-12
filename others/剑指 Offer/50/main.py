class Solution:
    def firstUniqChar(self, s: str) -> str:
        count = dict()
        for c in s:
            if c in count.keys():
                count[c] += 1
            else:
                count[c] = 1
        for c in s:
            if count[c] == 1:
                return c
        return ''