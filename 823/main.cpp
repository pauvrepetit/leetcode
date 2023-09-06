/*
 * @lc app=leetcode.cn id=823 lang=cpp
 *
 * [823] 带因子的二叉树
 */
#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    int numFactoredBinaryTrees(vector<int>& arr) {
        std::unordered_map<int, long long> count;
        long long all_count = 0;
        std::sort(arr.begin(), arr.end());
        for (int i = 0; i < arr.size(); i++) {
            long long local_count = 1;
            for (int j = 0; j < i; j++) {
                if (arr[i] % arr[j] == 0 && count.find(arr[i] / arr[j]) != count.end()) {
                    local_count += count[arr[j]] * count[arr[i] / arr[j]];
                    local_count %= 1000000007;
                }
            }
            count[arr[i]] = local_count;
            all_count += local_count;
            all_count %= 1000000007;
        }
        return all_count;
    }
};
// @lc code=end

