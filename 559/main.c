#include <stdlib.h>
#include <stdio.h>
/*
 * @lc app=leetcode.cn id=559 lang=c
 *
 * [559] N 叉树的最大深度
 */

// @lc code=start
/**
 * Definition for a Node.
 * struct Node {
 *     int val;
 *     int numChildren;
 *     struct Node** children;
 * };
 */

int max(int a, int b) {
    return a > b ? a : b;
}

int maxDepth(struct Node* root) {
    if (root == NULL) {
        return 0;
    }
    int dep = 0;
    for (int i = 0; i < root->numChildren; i++) {
        dep = max(dep, maxDepth(root->children[i]));
    }
    return dep + 1;
}
// @lc code=end

