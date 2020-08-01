# 833. 字符串中的查找与替换
#
# 20200801
# huao
# 这个题目已经给了查找/替换的子串的位置 根据其给定的位置判断是否匹配 如果匹配 进行替换即可
# 需要注意替换以后会影响到后面的索引值

from typing import List


class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        length = len(indexes)
        replace = []
        for i in range(length):
            replace.append([indexes[i], sources[i], targets[i]])
        replace.sort(key=lambda x: x[0])
        i = 0
        while i < length:
            if S[replace[i][0]:].startswith(replace[i][1]):
                S = S[:replace[i][0]] + S[replace[i][0]:].replace(replace[i][1], replace[i][2], 1)
                delta = len(replace[i][2]) - len(replace[i][1])
                for j in range(i+1, length):
                    replace[j][0] += delta
            i += 1
        return S


sol = Solution()
print(sol.findReplaceString("ehvfwtrvcodllgjctguxeicjoudmxbevzrvravkidnricwsbnxmxvdckzahmqzbrlqugtmjvoqbxarmlgjeqcorhnodvnoqfomdp",
                            [1, 31, 44, 70, 23, 73, 76, 92, 90, 86, 42, 4, 50, 17, 53, 20, 55,
                                15, 38, 64, 25, 9, 7, 68, 60, 88, 96, 47, 57, 34, 81, 78, 28],
                            ["hvf", "vzr", "cw", "jvo", "jo", "qb", "ar", "noqf", "dv", "rh", "ri", "wt", "mx", "gux", "dc", "eic", "kz",
                                "ct", "kidn", "lq", "ud", "odll", "vc", "tm", "qz", "no", "om", "bn", "ahm", "vra", "jeqco", "ml", "xb"],
                            ["ajq", "zb", "r", "fai", "e", "zs", "io", "snxd", "nw", "oi", "ofb", "quq", "gj", "nsys", "dk", "sf", "muj", "ll", "hqx", "k", "n", "ptrya", "f", "qek", "u", "dhj", "e", "kr", "waj", "rvkr", "roaoeq", "mci", "djw"]))

# "ehvfwtrvcodllgjctguxeicjoudmxbevzrvravkidnricwsbnxmxvdckzahmqzbrlqugtmjvoqbxarmlgjeqcorhnodvnoqfomdp"
# eajqquqrfptryagjllnsyssfenmdjwezbrvkrvhqxofbrskrxgjvdkmujwajubrkugqekfaizsxiomcigroaoeqoidhjnwsnxdedp
# eajqquqrfptryagjllnsyssfenmdjwezbrvkrvhqxofbrskrxgjvdkmujwajubrkugqekfaizsxiomcigroaoeqoidhjnwsnxdedp