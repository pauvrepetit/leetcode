from typing import List

class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        p_list = [[], [0b0, 0b1]]
        for i in range(2, n + 1):
            p = p_list[-1]
            next_p = [value + 2 ** (i-1) for value in p]
            p += next_p[::-1]
            p_list.append(p)
        p = p_list[-1]
        for i in range(len(p)):
            if p[i] == start:
                return p[i:] + p[:i]
        return []

print(Solution().circularPermutation(2, 3))
print(Solution().circularPermutation(3, 2))
