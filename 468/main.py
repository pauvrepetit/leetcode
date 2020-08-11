# 468. 验证IP地址
#
# 20200811
# huao
# 这字符串的处理 就有很多细节要考虑到 容易出错

class Solution:
    def validIPAddress(self, IP: str) -> str:
        if '.' in IP:
            # IPv4
            numList = IP.split('.')
            if len(numList) != 4:
                return "Neither"
            for num in numList:
                for c in num:
                    if c not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                        return "Neither"
                if len(num) == 1:
                    continue
                elif len(num) == 0 or num[0] == '0' or int(num) >= 256:
                    return "Neither"
            return "IPv4"
        else:
            # IPv6
            numList = IP.split(':')
            if len(numList) != 8:
                return "Neither"
            for num in numList:
                if len(num) == 1 and num[0] == '0':
                    continue
                elif len(num) <= 4 and len(num) > 0:
                    for c in num:
                        if c not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F']:
                            return "Neither"
                else:
                    return "Neither"
            return "IPv6"
