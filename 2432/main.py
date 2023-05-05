from typing import List

#
# @lc app=leetcode.cn id=2432 lang=python3
#
# [2432] 处理用时最长的那个任务的员工
#

# @lc code=start
class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        for i in range(1, len(logs))[::-1]:
            logs[i][1] = logs[i][1] - logs[i - 1][1]
        max_time = 0
        max_time_id = 0
        for id, time in logs:
            if time > max_time:
                max_time = time
                max_time_id = id
            elif time == max_time and max_time_id > id:
                max_time_id = id
        return max_time_id
# @lc code=end

