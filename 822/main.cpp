/*
 * @lc app=leetcode.cn id=822 lang=cpp
 *
 * [822] 翻转卡片游戏
 */
#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    int flipgame(vector<int>& fronts, vector<int>& backs) {
        std::unordered_set<int> nums;
        std::unordered_set<int> non_nums;
        // for (auto && n : fronts) {
        //     nums.insert(n);
        // }
        // for (auto && n : backs) {
        //     nums.insert(n);
        // }
        // for ()
        for (int i = 0; i < fronts.size(); i++) {
            nums.insert(fronts[i]);
            nums.insert(backs[i]);
            if (fronts[i] == backs[i]) {
                non_nums.insert(fronts[i]);
            }
        }
        int min_num = 3000;
        for (auto && num : nums) {
            if (non_nums.find(num) == non_nums.end()) {
                min_num = std::min(min_num, num);
            }
        }
        if (min_num == 3000) min_num = 0;
        return min_num;
    }
};
// @lc code=end

