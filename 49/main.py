# 49. 字母异位词分组

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for s in strs:
            ss = ''.join(c for c in sorted(s))
            if ss in group.keys():
                group[ss].append(s)
            else:
                group[ss] = [s]
        return list(group.values())
