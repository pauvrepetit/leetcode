# 205. 同构字符串
#
# 20200801
# huao
# 维护一个映射关系(字典)
# 如果出现冲突的映射，就返回False
# 如果不存在冲突，则True

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        charMapS = {}
        charMapT = {}
        strLen = len(s)
        if s == t:
            return True
        for i in range(strLen):
            if s[i] in charMapS.keys():
                if t[i] != charMapS[s[i]]:
                    return False
            else:
                charMapS[s[i]] = t[i]
            
            if t[i] in charMapT.keys():
                if s[i] != charMapT[t[i]]:
                    return False
            else:
                charMapT[t[i]] = s[i]
        return True
