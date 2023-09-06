/*
 * @lc app=leetcode.cn id=5 lang=cpp
 *
 * [5] 最长回文子串
 */
#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    string longestPalindrome(string s) {
        string longest_str;
        for (int i = 0; i < s.size(); i++) {
            // 以s[i]为中心
            string local_longest_str = s.substr(i, 1);
            for (int j = i-1, k = i+1; j >= 0 && k < s.size(); j--, k++) {
                if (s[j] == s[k]) {
                    local_longest_str = s.substr(j, k-j+1);
                } else {
                    break;
                }
            }
            if (local_longest_str.size() > longest_str.size()) {
                longest_str = local_longest_str;
            }
            // 以s[i]s[i+1]为中心
            if (i < s.size() - 1 && s[i] == s[i+1]) {
                local_longest_str = s.substr(i, 2);
                for (int j = i-1, k = i+2; j >= 0 && k < s.size(); j--, k++) {
                    if (s[j] == s[k]) {
                        local_longest_str = s.substr(j, k-j+1);
                    } else {
                        break;
                    }
                }
            }
            if (local_longest_str.size() > longest_str.size()) {
                longest_str = local_longest_str;
            }
        }
        return longest_str;
    }
};
// @lc code=end

