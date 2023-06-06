#include <stdlib.h>
/*
 * @lc app=leetcode.cn id=2611 lang=c
 *
 * [2611] 老鼠和奶酪
 */

// @lc code=start
int comp(int *a, int *b) {
    return *b - *a;
}

int miceAndCheese(int* reward1, int reward1Size, int* reward2, int reward2Size, int k){
    int scores = 0;
    for (int i = 0; i < reward2Size; i++) {
        scores += reward2[i];
        reward1[i] -= reward2[i];
    }
    qsort(reward1, reward1Size, sizeof(int), comp);
    for (int i = 0; i < k; i++) {
        scores += reward1[i];
    }
    return scores;
}
// @lc code=end
