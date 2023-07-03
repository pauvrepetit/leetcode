class Solution:
    def isInt(self, s: str) -> bool:
        if len(s) == 0:
            return False
        if s[0] in "+-":
            s = s[1:]
        if len(s) == 0:
            return False
        for i in s:
            if i not in "0123456789":
                return False
        return True

    def isDouble(self, s: str) -> bool:
        if len(s) == 0:
            return False
        if s[0] in "+-":
            s = s[1:]
        if len(s) == 0:
            return False
        if s[0] not in "0123456789.":
            return False
        if s.count(".") > 1:
            return False
        ss = s.split('.')
        while '' in ss:
            ss.remove('')
        if len(ss) == 0:
            return False
        for i in ss:
            for ii in i:
                if ii not in "0123456789":
                    return False
        return True

    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if 'e' in s:
            strs = s.split('e')
            if len(strs) != 2:
                return False
            return (self.isInt(strs[0]) or self.isDouble(strs[0])) and self.isInt(strs[1])
        if 'E' in s:
            strs = s.split('E')
            if len(strs) != 2:
                return False
            return (self.isInt(strs[0]) or self.isDouble(strs[0])) and self.isInt(strs[1])
        return self.isInt(s) or self.isDouble(s)

print(Solution().isNumber(".1"))

for s in ["+100", "5e2", "-123", "3.1416", "-1E-16", "0123", "0"]:
    print(Solution().isNumber(s))

for s in ["12e", "1a3.14", "1.2.3", "+-5", "12e+5.4", "e"]:
    print(Solution().isNumber(s))
