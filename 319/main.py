import math

class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))

sol = Solution()
print(sol.bulbSwitch(4))
