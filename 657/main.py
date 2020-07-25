# 657. 机器人能否返回原点
#
# 20200725
# huao
# 这个题已经简单的没意思了

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        row = 0
        column = 0
        for move in moves:
            if move == 'U':
                row += 1
            elif move == 'D':
                row -= 1
            elif move == 'L':
                column -= 1
            else:
                column += 1
        if row == 0 and column == 0:
            return True
        else:
            return False
