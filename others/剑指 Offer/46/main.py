class Solution:
    def translateNum(self, num: int) -> int:
        ns = str(num)
        count = [0 for _ in range(len(ns)+1)]
        count[-1] = 1
        count[-2] = 1
        for i in range(len(ns)-1)[::-1]:
            if ns[i] != '0' and int(ns[i:i+2]) < 26:
                count[i] = count[i+1] + count[i+2]
            else:
                count[i] = count[i+1]
        return count[0]

print(Solution().translateNum(506))
