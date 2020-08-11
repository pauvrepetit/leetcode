# 290. 单词规律
#
# 20200811
# huao
# 正向字典+反向字典

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        strList = str.split(' ')
        if len(pattern) != len(strList):
            return False
        length = len(pattern)
        posDic = {}
        negDic = {}
        for i in range(length):
            if pattern[i] in posDic.keys() and posDic[pattern[i]] == strList[i]:
                continue
            elif pattern[i] in posDic.keys() and posDic[pattern[i]] != strList[i]:
                return False
            else:
                if strList[i] in negDic.keys():
                    return False
                else:
                    posDic[pattern[i]] = strList[i]
                    negDic[strList[i]] = pattern[i]
        return True
