/* 剑指 Offer 57. 和为s的两个数字
 *
 * 20200727
 * huao
 * 
 * 二分查找
 * C++ STL就是好
 */

#include <algorithm>
#include <iostream>
#include <vector>

using std::binary_search;
using std::cout;
using std::endl;
using std::vector;

class Solution {
  public:
    vector<int> twoSum(vector<int> &nums, int target) {
        for (auto num = nums.begin(); num != nums.end(); num++) {
            if (binary_search(num, nums.end(), target - *num)) {
                vector<int> twoNum = {*num, target - *num};
                return twoNum;
            }
        }
        vector<int> twoNum = {};
        return twoNum;
    }
};

int main(void) {
    vector<int> nums = {2, 7, 11, 15};
    Solution sol = Solution();
    for (auto &num : sol.twoSum(nums, 9)) {
        cout << num << endl;
    }
    return 0;
}