# 401. 二进制手表
#
# 20200810
# huao
# 其实10位的二进制数并不多

class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        timeList = []
        for i in range(1024):
            if self.countOne(i) == num:
                hour = i // 64
                minute = i % 64
                if hour >= 12 or minute >= 60:
                    continue
                elif minute < 10:
                    timeList.append(str(hour) + ":0" + str(minute))
                else:
                    timeList.append(str(hour) + ":" + str(minute))
        return timeList

    def countOne(self, num: int) -> int:
        count = 0
        while num != 0:
            count += (num & 1)
            num >>= 1
        return count
