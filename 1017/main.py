# 1017. 负二进制转换
#
# 20200801
# huao
# 观察奇数位上的1，如果该位置为1，那么使用负二进制表示时，会比实际二进制时少2**(i+1)
# 把这个差值加进去，并进行处理加完以后的值
# 处理完以后，得到的数字的二进制表示就是原数的负二进制表示

class Solution:
    def baseNeg2(self, N: int) -> str:
        i = 0
        while N >= (1 << i):
            if i % 2 == 1 and (N & (1 << i) != 0):
                N += (2 << i)
            i += 1
        return bin(N)[2:]


sol = Solution()
print(sol.baseNeg2(4))
