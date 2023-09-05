/*
 * @lc app=leetcode.cn id=75 lang=cpp
 *
 * [75] 颜色分类
 */
#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int count[3] = {0, 0, 0};
        for (auto &&i : nums) {
            count[i]++;
        }
        for (int i = 0; i < nums.size(); i++) {
            if (i < count[0]) {
                nums[i] = 0;
            } else if (i < count[0] + count[1]) {
                nums[i] = 1;
            } else {
                nums[i] = 2;
            }
        }
    }
};
// @lc code=end

