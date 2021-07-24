# 1736. 替换隐藏数字得到的最晚时间
#
# 20210724
# huao

class Solution:
    def maximumTime(self, time: str) -> str:
        h1 = time[0]
        h2 = time[1]
        m1 = time[3]
        m2 = time[4]
        if h1 == '?' and h2 == '?':
            h1 = '2'
            h2 = '3'
        elif h1 == '?':
            h2 = int(h2)
            h1 = '1' if h2 >= 4 else '2'
            h2 = str(h2)
        elif h2 == '?':
            h1 = int(h1)
            h2 = '3' if h1 == 2 else '9'
            h1 = str(h1)
        else:
            pass

        if m1 == '?' and m2 == '?':
            m1 = '5'
            m2 = '9'
        elif m1 == '?':
            m1 = '5'
        elif m2 == '?':
            m2 = '9'
        else:
            pass

        return h1 + h2 + ":" + m1 + m2
