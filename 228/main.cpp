/*
 * @lc app=leetcode.cn id=228 lang=cpp
 *
 * [228] 汇总区间
 */
#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> res;
        if (nums.size() == 0) {
            return res;
        }
        int begin = nums[0];
        int end;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] != nums[i-1] + 1) {
                end = nums[i-1];
                if (begin == end) {
                    res.emplace_back(to_string(begin));
                } else {
                    res.emplace_back(to_string(begin) + "->" + to_string(end));
                }
                begin = nums[i];
            }
        }
        end = nums[nums.size() - 1];
        if (begin == end) {
            res.emplace_back(to_string(begin));
        } else {
            res.emplace_back(to_string(begin) + "->" + to_string(end));
        }
        return res;
    }
};
// @lc code=end

