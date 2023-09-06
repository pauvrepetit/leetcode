/*
 * @lc app=leetcode.cn id=2240 lang=cpp
 *
 * [2240] 买钢笔和铅笔的方案数
 */

// @lc code=start
class Solution {
public:
    long long waysToBuyPensPencils(int total, int cost1, int cost2) {
        long long all_count = 0;
        for (int i = 0; i <= total / cost1; i++) {
            // 买i个cost1的情况
            int left = total - cost1 * i;
            all_count += left / cost2 + 1;
        }
        return all_count;
    }
};
// @lc code=end

