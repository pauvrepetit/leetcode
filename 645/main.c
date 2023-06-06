#include <stdlib.h>
#include <stdio.h>
#include <string.h>
/*
 * @lc app=leetcode.cn id=645 lang=c
 *
 * [645] 错误的集合
 */

// @lc code=start


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findErrorNums(int* nums, int numsSize, int* returnSize){
    *returnSize = 2;
    int *result = (int *)malloc(sizeof(int) * 2);
    char *tmp = (char *)malloc(sizeof(char) * numsSize);
    memset(tmp, 0, sizeof(char) * numsSize);
    for (int i = 0; i < numsSize; i++) {
        tmp[nums[i]-1]++;
    }
    int two = 0;
    int zero = 0;
    for (int i = 0; i < numsSize; i++) {
        if (tmp[i] == 0) {
            zero = i + 1;
        }
        if (tmp[i] == 2) {
            two = i + 1;
        }
    }
    result[0] = two;
    result[1] = zero;
    return result;
}
// @lc code=end

