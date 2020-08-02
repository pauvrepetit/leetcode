/* 113. 路径总和 II
 * 剑指 Offer 34. 二叉树中和为某一值的路径
 *
 * 20200802
 * huao
 * 那么问题来了 为啥我写的C++也这么慢呢...
 */

#include <stdio.h>
#include <vector>

using std::vector;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
  public:
    vector<vector<int>> pathSum(TreeNode *root, int sum) {
        vector<int> route;
        return pathSum(root, sum, 0, route);
    }

    vector<vector<int>> pathSum(TreeNode *root, int sum, int nowSum, vector<int> route) {
        vector<vector<int>> routeList;
        if (root == NULL) {
            return routeList;
        }
        route.push_back(root->val);
        if (root->left == NULL and root->right == NULL) {
            if (root->val + nowSum == sum)
                routeList.push_back(route);
            return routeList;
        } else {
            vector<vector<int>> left = pathSum(root->left, sum, nowSum + root->val, route);
            vector<vector<int>> right = pathSum(root->right, sum, nowSum + root->val, route);
            routeList.insert(routeList.end(), left.begin(), left.end());
            routeList.insert(routeList.end(), right.begin(), right.end());
            return routeList;
        }
    }
};