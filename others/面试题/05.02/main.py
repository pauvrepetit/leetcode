class Solution:
    def printBin(self, num: float) -> str:
        res = "0."
        half = 0.5
        threshold = 1e-8
        for _ in range(7):
            if num - half > threshold:
                num = num - half
                res += "1"
            elif abs(num - half) < threshold:
                return res + "1"
            else:
                res += "0"
            half = half / 2
        return "ERROR"

print(Solution().printBin(0.625))
print(Solution().printBin(0.1))
