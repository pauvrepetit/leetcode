

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        v1Len = len(v1)
        v2Len = len(v2)
        if v1Len > v2Len:
            v2 += [0] * (v1Len - v2Len)
        else:
            v1 += [0] * (v2Len - v1Len)

        for i in range(len(v1)):
            if v1[i] == v2[i]:
                continue
            elif v1[i] > v2[i]:
                return 1
            else:
                return -1
        return 0


print(Solution().compareVersion(version1="0.1", version2="1.1"))
print(Solution().compareVersion(version1="1.0.1", version2="1"))
print(Solution().compareVersion(version1="7.5.2.4", version2="7.5.3"))
print(Solution().compareVersion(version1="1.01", version2="1.001"))
print(Solution().compareVersion(version1="1.0", version2="1.0.0"))
