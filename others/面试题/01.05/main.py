# 面试题 01.05. 一次编辑
#
# 20200912
# huao

def check(longer: str, shorter: str) -> bool:
    flag = 0
    for i in range(len(shorter)):
        if longer[i+flag] == shorter[i]:
            continue
        elif flag == 0:
            flag = 1
            return longer[i+flag:] == shorter[i:]
        else:
            return False
    return True


def checkSame(first, second):
    flag = 0
    for i in range(len(first)):
        if first[i] == second[i]:
            continue
        else:
            return first[i+1:] == second[i+1:]
    return True


class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        firstLen = len(first)
        secondLen = len(second)
        if firstLen == secondLen:
            return first == second or checkSame(first, second)
        elif firstLen == secondLen + 1:
            return check(first, second)
        elif firstLen == secondLen - 1:
            return check(second, first)
        else:
            return False
