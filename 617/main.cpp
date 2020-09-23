/*
 * 617. 合并二叉树
 *
 * 20200923
 * Hu Ao
 */

#include <cstdio>

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
  TreeNode *mergeTrees(TreeNode *t1, TreeNode *t2) {
    if (t1 == NULL && t2 == NULL) {
      return NULL;
    } else if (t2 == NULL) {
      return t1;
    } else if (t1 == NULL) {
      return t2;
    } else {
      TreeNode *root = new TreeNode(t1->val + t2->val);
      root->left = mergeTrees(t1->left, t2->left);
      root->right = mergeTrees(t1->right, t2->right);
      return root;
    }
  }
};