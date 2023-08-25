/*
 * @lc app=leetcode.cn id=516 lang=cpp
 *
 * [516] 最长回文子序列
 */
#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    int longestPalindromeSubseq(string s) {
        vector<vector<int>> strs;
        for (int i = 0; i < s.size(); i++) {
            vector<int> tmp;
            for (int j = 0; j < s.size(); j++) {
                tmp.emplace_back(0xFFFFFFF);
            }
            tmp[i] = 1;
            strs.push_back(tmp);
        }
        std::stack<std::pair<std::pair<int, int>, bool>> q;
        q.emplace(std::make_pair(0, s.size()-1), false);
        while (!q.empty()) {
            auto pair = q.top();
            q.pop();
            int i = pair.first.first;
            int j = pair.first.second;
            bool status = pair.second;

            if (i > j) {
                strs[i][j] = 0;
                continue;
            }
            if (strs[i][j] != 0xFFFFFFF) {
                continue;
            }

            if (s[i] == s[j]) {
                if (status) {
                    strs[i][j] = strs[i+1][j-1] + 2;
                } else {
                    q.emplace(std::make_pair(i, j), true);
                    q.emplace(std::make_pair(i+1, j-1), false);
                }
            } else {
                if (status) {
                    strs[i][j] = std::max(strs[i+1][j], strs[i][j-1]);
                } else {
                    q.emplace(std::make_pair(i, j), true);
                    q.emplace(std::make_pair(i, j-1), false);
                    q.emplace(std::make_pair(i+1, j), false);
                }
            }
        }
        return strs[0][s.size()-1];
    }
};
// @lc code=end

