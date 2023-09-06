/*
 * @lc app=leetcode.cn id=1123 lang=cpp
 *
 * [1123] 最深叶节点的最近公共祖先
 */
#include <bits/stdc++.h>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    std::pair<TreeNode *, std::pair<int, int>> func(TreeNode *root) {
        if (root == nullptr) {
            return std::make_pair(root, std::make_pair(0, 0));
        }
        auto left_res = func(root->left);
        auto right_res = func(root->right);
        if (left_res.second.second == right_res.second.second) {
            return std::make_pair(root, std::make_pair(left_res.second.second + 1, left_res.second.second + 1));
        }
        if (left_res.second.second > right_res.second.second) {
            return std::make_pair(left_res.first, std::make_pair(left_res.second.first, left_res.second.second + 1));
        } else {
            return std::make_pair(right_res.first, std::make_pair(right_res.second.first, right_res.second.second + 1));
        }
    }

    TreeNode* lcaDeepestLeaves(TreeNode* root) {
        return func(root).first;
    }
};
// @lc code=end

