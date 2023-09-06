/*
 * @lc app=leetcode.cn id=1267 lang=cpp
 *
 * [1267] 统计参与通信的服务器
 */
#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
   public:
    int countServers(vector<vector<int>>& grid) {
        vector<int> row_count(grid.size());
        vector<int> col_count(grid[0].size());
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[i].size(); j++) {
                row_count[i] += grid[i][j];
                col_count[j] += grid[i][j];
            }
        }
        int count = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[i].size(); j++) {
                if (grid[i][j] == 1 && (row_count[i] >= 2 || col_count[j] >= 2)) {
                    count++;
                }
            }
        }
        return count;
    }
};
// @lc code=end
