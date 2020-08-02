# 868. 二进制间距
#
# 20200802
# huao
# 右移 看最低位是否为1
# 记录上次看到的1的位置 和当前位置比较即可

class Solution:
    def binaryGap(self, N: int) -> int:
        lasti = -1
        i = 0
        maxGap = -1
        while N != 0:
            if N & 1 != 0:
                if lasti != -1:
                    maxGap = max(i - lasti, maxGap)
                lasti = i
            i += 1
            N >>= 1
        return maxGap
