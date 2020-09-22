/* 剑指 Offer 53 - I. 在排序数组中查找数字 I
 *
 * 20200730
 * huao
 * 二分查找
 */

#include <algorithm>
#include <vector>

using std::lower_bound;
using std::upper_bound;
using std::vector;

class Solution {
  public:
    int search(vector<int> &nums, int target) {
        auto left = lower_bound(nums.begin(), nums.end(), target);
        auto right = upper_bound(nums.begin(), nums.end(), target);
        return right - left;
    }
};