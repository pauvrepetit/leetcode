/*
 * @lc app=leetcode.cn id=1448 lang=cpp
 *
 * [1448] 统计二叉树中好节点的数目
 */

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
    int goodNodes(TreeNode* root, int max_val) {
        if (root == nullptr) {
            return 0;
        }
        if (root->val >= max_val) {
            return 1 + goodNodes(root->left, root->val) + goodNodes(root->right, root->val);
        } else {
            return goodNodes(root->left, max_val) + goodNodes(root->right, max_val);
        }
    }

    int goodNodes(TreeNode* root) {
        return goodNodes(root, -0xFFFFFF);
    }
};
// @lc code=end

