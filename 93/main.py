# 93. 复原IP地址
#
# 20200809
# huao
# 根据长度遍历一下 3*3*3=27可能的情况

from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        sLen = len(s)
        IpList = []
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    if i+j+k >= sLen:
                        break
                    if s[0] == '0' and i != 1:
                        continue
                    if s[i] == '0' and j != 1:
                        continue
                    if s[i+j] == '0' and k != 1:
                        continue
                    if s[i+j+k] == '0' and (sLen-i-j-k) != 1:
                        continue
                    num1 = int(s[:i])
                    num2 = int(s[i:i+j])
                    num3 = int(s[i+j:i+j+k])
                    num4 = int(s[i+j+k:])
                    if num1 < 256 and num2 < 256 and num3 < 256 and num4 < 256:
                        IpList.append(str(num1) + "." + str(num2) +
                                      "." + str(num3) + "." + str(num4))
        return IpList


sol = Solution()
# print(sol.restoreIpAddresses("25525511135"))
print(sol.restoreIpAddresses("010010"))
