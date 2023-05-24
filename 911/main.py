from typing import List
import bisect
#
# @lc app=leetcode.cn id=911 lang=python3
#
# [911] 在线选举
#

# @lc code=start
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times[:]
        self.winners = []
        votes = dict()
        ordered_votes = []
        for i in range(len(times)):
            p = persons[i]
            if p in votes.keys():
                ordered_votes.remove((votes[p], p))
                votes[p] += 1
                bisect.insort_right(ordered_votes, (votes[p], p), key=lambda x: x[0])
            else:
                votes[p] = 1
                bisect.insort_right(ordered_votes, (votes[p], p), key=lambda x: x[0])
            self.winners.append(ordered_votes[-1][1])


    def q(self, t: int) -> int:
        i = bisect.bisect_left(self.times, t)
        if i == len(self.times) or self.times[i] != t:
            i -= 1
        return self.winners[i]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
# @lc code=end

obj = TopVotedCandidate([0,1,1,0,0,1,0],[0,5,10,15,20,25,30])
print(obj.q(3))
print(obj.q(12))