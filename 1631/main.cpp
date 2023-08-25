/*
 * @lc app=leetcode.cn id=1631 lang=cpp
 *
 * [1631] 最小体力消耗路径
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start

class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        vector<vector<int>> loss;
        for (int i = 0; i < heights.size(); i++) {
            vector<int> tmp;
            tmp.reserve(heights[i].size());
            for (int j = 0; j < heights[i].size(); j++) {
                tmp.push_back(0xFFFFFFF);
            }
            loss.push_back(tmp);
            // printf("push %d/%d\n", i, heights.size());
        }
        // printf("%d %d\n", loss.size(), loss[0].size());
        loss[0][0] = 0;
        std::queue<std::pair<int, int>> q;
        q.emplace(0, 0);
        while (!q.empty()) {
            auto pair = q.front();
            q.pop();
            int i = pair.first;
            int j = pair.second;
            int old_val;
            int new_val;

            if (j+1 < loss[i].size()) {
                old_val = loss[i][j+1];
                new_val = std::max(loss[i][j], std::abs(heights[i][j] - heights[i][j+1]));
                if (new_val < old_val) {
                    loss[i][j+1] = new_val;
                    q.emplace(i, j+1);
                }
            }
            if (i+1 < loss.size()) {
                old_val = loss[i+1][j];
                new_val = std::max(loss[i][j], std::abs(heights[i][j] - heights[i+1][j]));
                if (new_val < old_val) {
                    loss[i+1][j] = new_val;
                    q.emplace(i+1, j);
                }
            }
            if (i-1 >= 0) {
                old_val = loss[i-1][j];
                new_val = std::max(loss[i][j], std::abs(heights[i][j] - heights[i-1][j]));
                if (new_val < old_val) {
                    loss[i-1][j] = new_val;
                    q.emplace(i-1, j);
                }
            }
            if (j-1 >= 0) {
                old_val = loss[i][j-1];
                new_val = std::max(loss[i][j], std::abs(heights[i][j] - heights[i][j-1]));
                if (new_val < old_val) {
                    loss[i][j-1] = new_val;
                    q.emplace(i, j-1);
                }
            }
        }
        // printf("%d %d\n", heights.size(), heights[0].size());
        // printf("%d %d\n", loss.size(), loss[0].size());
        // for (int i = 0; i < loss.size(); i++) {
        //     for (int j = 0; j < loss[i].size(); j++) {
        //         printf("%d ", loss[i][j]);
        //     }
        //     printf("\n");
        // }
        return loss[loss.size()-1][loss[0].size()-1];
    }
};
// @lc code=end

