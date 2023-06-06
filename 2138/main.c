#include <string.h>
#include <stdlib.h>
/*
 * @lc app=leetcode.cn id=2138 lang=c
 *
 * [2138] 将字符串拆分为若干长度为 k 的组
 */

// @lc code=start


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char ** divideString(char * s, int k, char fill, int* returnSize){
    int len = strlen(s);
    *returnSize = (len % k == 0 ? len / k : len / k + 1);
    char **result = (char *)malloc(sizeof(char *) * *returnSize);
    int p = 0;
    for (int i = 0; i < *returnSize - 1; i++) {
        result[i] = (char *)malloc(sizeof(char) * (k + 1));
        result[i][k] = '\0';
        for (int j = 0; j < k; j++) {
            result[i][j] = s[p++];
        }
    }
    result[*returnSize - 1] = (char *)malloc(sizeof(char) * (k + 1));
    result[*returnSize - 1][k] = '\0';
    int last_len = k;
    if (len % k != 0) last_len = len % k;
    for (int j = 0; j < last_len; j++) result[*returnSize - 1][j] = s[p++];
    for (int j = last_len; j < k; j++) result[*returnSize - 1][j] = fill;

    return result;
}
// @lc code=end

