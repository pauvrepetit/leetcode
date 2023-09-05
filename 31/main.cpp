/*
 * @lc app=leetcode.cn id=31 lang=cpp
 *
 * [31] 下一个排列
 */
#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int loc = 0;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] > nums[i-1]) {
                loc = i;
            }
        }
        if (loc == 0) {
            std::sort(nums.begin(), nums.end());
        } else {
            int loc_val = nums[loc-1];
            for (int i = nums.size()-1; i >= loc; i--) {
                if (nums[i] > loc_val) {
                    loc_val = nums[i];
                    nums[i] = nums[loc-1];
                    nums[loc-1] = loc_val;
                    break;
                }
            }
            std::sort(nums.begin() + loc, nums.end());
        }
    }
};
// @lc code=end

