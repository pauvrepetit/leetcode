#include <stdio.h>
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {
    int * num = (int *)malloc(sizeof(int) * 2);
    int i = 0, j = 0;
    for(i = 0; i < numsSize; i++) {
        for (j = i + 1; j < numsSize; j++) {
            if (nums[i] + nums[j] == target) {
                num[0] = i;
                num[1] = j;
                return num;
            }
        }
    }
    return 0;
}

int main() {
    int nums[4] = {2, 7, 11, 15};
    printf("%d %d\n", twoSum(nums, 4, 9)[0], twoSum(nums, 4, 9)[1]);
    return 0;
}