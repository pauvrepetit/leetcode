# 649. Dota2 参议院
# 贪心

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        while True:
            rloc = senate.find('R')
            dloc = senate.find('D')
            if rloc == -1:
                return 'Dire'
            elif dloc == -1:
                return 'Radiant'
            else:
                if senate[0] == 'R':
                    senate = senate[1:dloc] + senate[dloc+1:] + 'R'
                else:
                    senate = senate[1:rloc] + senate[rloc+1:] + 'D'
