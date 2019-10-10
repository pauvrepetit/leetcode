class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        start_1 = start.replace('X', '')
        end_1 = end.replace('X', '')
        bool1 = (start_1 == end_1)
        count_R1 = 0
        count_R2 = 0
        count_L1 = 0
        count_L2 = 0
        for i in range(len(start)):
            if start[i] == 'R':
                count_R1 += 1
            if end[i] == 'R':
                count_R2 += 1
            if count_R1 < count_R2:
                return False
        
        for i in range(len(start))[:-1:]:
            if start[i] == 'L':
                count_L1 += 1
            if end[i] == 'L':
                count_L2 += 1
            if count_L1 > count_L2:
                return False
        return bool1

sol = Solution()
print(sol.canTransform("RXXLRXRXL", "XRLXXRRLX"))
print(sol.canTransform("XXRXXLXXXX", "XXXXRXXLXX"))
