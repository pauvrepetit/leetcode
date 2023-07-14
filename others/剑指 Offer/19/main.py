class Solution:
    def match(self, s: str, p: str) -> bool:
        if p == "":
            return s == ""
        if s == "":
            for c in p:
                if c in 'abcdefghijklmnopqrstuvwxyz.':
                    return False
            return True
        if p[0] in 'abcdefghijklmnopqrstuvwxyz':
            if s[0] != p[0]:
                return False
            else:
                return self.match(s[1:], p[1:])
        if p[0] == '.':
            return self.match(s[1:], p[1:])
        if p[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            for i in range(len(s)+1):
                if s[:i] == p[0].lower() * i:
                    if self.match(s[i:], p[1:]):
                        return True
                    continue
                return False
        if p[0] == '-':
            for i in range(len(s)+1):
                if self.match(s[i:], p[1:]):
                    return True
        return False

    def isMatch(self, s: str, p: str) -> bool:
        if p == "":
            return s == ""
        ss = ""
        for i in range(len(p)-1):
            if p[i+1] == '*':
                if p[i] == '.':
                    ss += '-'
                else:
                    ss += p[i].upper()
            elif p[i] == '*':
                continue
            else:
                ss += p[i]
        if p[-1] != '*':
            ss += p[-1]
        return self.match(s, ss)

print(Solution().isMatch("aa", ""))
