# 796. 旋转字符串
#
# 20200728
# huao
# 这个好像和前面某个题一样的...
# 遍历，判断一下就好了

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A == '' and B == '':
            return True
        lenA = len(A)
        lenB = len(B)
        if lenA != lenB:
            return False
        for i in range(lenA):
            if A[:i] == B[lenA-i:] and A[i:] == B[:lenA-i]:
                return True
        return False
