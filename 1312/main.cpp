/*
 * @lc app=leetcode.cn id=1312 lang=cpp
 *
 * [1312] 让字符串成为回文串的最少插入次数
 */
#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    // int compute(string s, int count[510][510], int i, int j) {
    //     if (i > j) {
    //         return 0;
    //     }
    //     if (count[i][j] != 0xFFFFFFF) {
    //         return count[i][j];
    //     }
    //     if (s[i] == s[j]) {
    //         count[i][j] = compute(s, count, i+1, j-1);
    //     } else {
    //         count[i][j] = std::min(compute(s, count, i+1, j), compute(s, count, i, j-1)) + 1;
    //     }
    //     return count[i][j];
    // }

    // int minInsertions(string s) {
    //     int count[510][510];    // 记录子串s[i:j]的结果(包含i和j)
    //     for (int i = 0; i < s.size(); i++) {
    //         for (int j = 0; j < s.size(); j++) {
    //             count[i][j] = 0xFFFFFFF;
    //         }
    //         count[i][i] = 0;
    //     }
    //     return compute(s, count, 0, s.size()-1);
    // }


    int minInsertions(string s) {
        int count[510][510];    // 记录子串s[i:j]的结果(包含i和j)
        for (int i = 0; i < s.size(); i++) {
            for (int j = 0; j < s.size(); j++) {
                count[i][j] = 0xFFFFFFF;
            }
            count[i][i] = 0;
        }
        // return compute(s, count, 0, s.size()-1);
        std::stack<std::pair<std::pair<int, int>, bool>> q;
        q.emplace(std::make_pair(0, s.size()-1), false);
        while (!q.empty()) {
            auto pair = q.top();
            q.pop();
            int i = pair.first.first;
            int j = pair.first.second;
            bool status = pair.second;
            if (i > j) {
                count[i][j] = 0;
                continue;
            }
            if (count[i][j] != 0xFFFFFFF) {
                continue;
            }
            if (s[i] == s[j]) {
                if (status) {
                    count[i][j] = count[i+1][j-1];
                } else {
                    q.emplace(std::make_pair(i, j), true);
                    q.emplace(std::make_pair(i+1, j-1), false);
                }
                // count[i][j] = compute(s, count, i+1, j-1);
            } else {
                if (status) {
                    count[i][j] = std::min(count[i+1][j], count[i][j-1]) + 1;
                } else {
                    q.emplace(std::make_pair(i, j), true);
                    q.emplace(std::make_pair(i+1, j), false);
                    q.emplace(std::make_pair(i, j-1), false);
                }
                // count[i][j] = std::min(compute(s, count, i+1, j), compute(s, count, i, j-1)) + 1;
            }
            // return count[i][j];
        }
        return count[0][s.size()-1];
    }
};
// @lc code=end

int main() {
    Solution s;
    int i = s.minInsertions("zjveiiwvc");
    printf("%d\n", i);
    return 0;
}