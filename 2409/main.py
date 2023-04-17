#
# @lc app=leetcode.cn id=2409 lang=python3
#
# [2409] 统计共同度过的日子数
#

# @lc code=start
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        arA = (int(arriveAlice[:2]), int(arriveAlice[3:]))
        leA = (int(leaveAlice[:2]), int(leaveAlice[3:]))
        arB = (int(arriveBob[:2]), int(arriveBob[3:]))
        leB = (int(leaveBob[:2]), int(leaveBob[3:]))
        if leA < arB or leB < arA:
            return 0
        tmp = [arA, leA, arB, leB]
        tmp.sort()
        overlap_begin = tmp[1]
        overlap_end = tmp[2]
        if overlap_begin[0] == overlap_end[0]:
            return overlap_end[1] - overlap_begin[1] + 1
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        overlap_days = days[overlap_begin[0] - 1] - overlap_begin[1] + 1
        overlap_days += overlap_end[1]
        for i in range(overlap_begin[0] + 1, overlap_end[0]):
            overlap_days += days[i - 1]
        return overlap_days
# @lc code=end

