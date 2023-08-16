/*
 * @lc app=leetcode.cn id=2682 lang=cpp
 *
 * [2682] 找出转圈游戏输家
 */
#include <bits/stdc++.h>

using std::vector;

// @lc code=start
class Solution {
public:
    vector<int> circularGameLosers(int n, int k) {
        vector<bool> visited(n);
        int i = 0;
        for (i = 0; i < n; i++) {
            visited[i] = false;
        }
        i = 0;
        int j = 1;
        while (!visited[i]) {
            visited[i] = true;
            // std::cout << i << std::endl;
            i = (i + j * k) % n;
            j++;
        }
        vector<int> res;
        for (i = 0; i < n; i++) {
            if (!visited[i]) {
                res.push_back(i+1);
            }
        }
        return res;
    }
};
// @lc code=end

// int main(void) {
//     Solution s;
//     // std::cout << s.circularGameLosers(5,2) << std::endl;
//     auto a = s.circularGameLosers(5,2);
//     for (auto &&i : a)
//     {
//         std::cout << i << std::endl;
//     }
//     return 0;
// }