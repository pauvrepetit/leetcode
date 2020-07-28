# 551. 学生出勤记录 I
#
# 20200728
# huao
# 找子串即可

class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A') <= 1 and s.count('LLL') == 0:
            return True
        else:
            return False
