# 859. 亲密字符串
#
# 20200811
# huao

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        lenA = len(A)
        lenB = len(B)
        if lenA != lenB:
            return False

        if A == B:
            char = [0 for i in range(26)]
            for c in A:
                char[ord(c) - ord('a')] += 1
                if char[ord(c) - ord('a')] > 1:
                    return True
            return False

        missLoc = []
        for i in range(lenA):
            if A[i] != B[i]:
                missLoc.append(i)
        if len(missLoc) != 2:
            return False
        if A[missLoc[0]] == B[missLoc[1]] and A[missLoc[1]] == B[missLoc[0]]:
            return True
        return False
