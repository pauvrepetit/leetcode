/*
 * @lc app=leetcode.cn id=2605 lang=cpp
 *
 * [2605] 从两个数字数组里生成最小数字
 */
#include <bits/stdc++.h>

using namespace std;

// @lc code=start
class Solution {
   public:
    int minNumber(vector<int>& nums1, vector<int>& nums2) {
        std::unordered_set<int> s1;
        int min1 = 10;
        int min2 = 10;
        for (auto&& i : nums1) {
            s1.insert(i);
            min1 = std::min(min1, i);
        }

        int min_num = 100;
        for (auto&& i : nums2) {
            if (s1.find(i) != s1.end()) {
                min_num = std::min(min_num, i);
            }
            min2 = std::min(min2, i);
        }

        min_num = std::min(min_num, std::min(min1, min2) * 10 + std::max(min1, min2));
        return min_num;
    }
};
// @lc code=end
