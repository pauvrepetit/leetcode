# 925. 长按键入
#
# 20200812
# huao

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0
        if len(name) == len(typed):
            return name == typed
        elif len(name) > len(typed):
            return False
        while i < len(name)-1:
            if j >= len(typed)-1:
                return False
            if name[i] != typed[j]:
                return False
            if name[i+1] == typed[j+1]:
                i += 1
                j += 1
            else:
                dup = typed[j]
                while j < len(typed) and typed[j] == dup:
                    j += 1
                i += 1
        if j >= len(typed):
            return False
        if name[i] == typed[j]:
            while j < len(typed):
                if typed[j] != name[i]:
                    return False
                j += 1
            return True


print(Solution().isLongPressedName("", ""))
