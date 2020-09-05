# 1461. 检查一个字符串是否包含所有长度为 K 的二进制子串
#
# 20200810
# huao

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        a = [0 for i in range(2**k)]
        count = 0
        for i in range(len(s)-k+1):
            num = int(s[i:i+k], 2)
            if a[num] == 0:
                count += 1
                a[num] = 1
        if count == 2**k:
            return True
        else:
            return False


print(Solution().hasAllCodes(s="00110110", k=2))
print(Solution().hasAllCodes(s="00110", k=2))
print(Solution().hasAllCodes(s="0110", k=1))
print(Solution().hasAllCodes(s="0110", k=2))
print(Solution().hasAllCodes(s="0000000001011100", k=4))
