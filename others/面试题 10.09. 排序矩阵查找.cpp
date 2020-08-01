/* 面试题 10.09. 排序矩阵查找
 *
 * 20200801
 * huao
 * 
 * 这写的就很傻...
 */
#include <algorithm>
#include <iostream>
#include <vector>

using std::cout;
using std::endl;
using std::lower_bound;
using std::vector;

class Solution {
  public:
    bool searchMatrix(vector<vector<int>> &matrix, int target) {
        for (int i = 0; i < matrix.size(); i++) {
            int column = lower_bound(matrix[i].begin(), matrix[i].end(), target) - matrix[i].begin();
            if (column < 0 || column >= matrix[i].size())
                continue;
            else if (matrix[i][column] == target)
                return true;
            else
                continue;
        }
        return false;
    }
};

int main(void) {
    Solution sol = Solution();
    vector<vector<int>> matrix;
    vector<int> v1;
    v1.push_back(5);
    matrix.push_back(v1);
    vector<int> v2;
    v2.push_back(6);
    matrix.push_back(v2);
    // vector<int> v1;
    // v1.push_back(1);
    // v1.push_back(4);
    // v1.push_back(7);
    // v1.push_back(11);
    // v1.push_back(15);
    // matrix.push_back(v1);
    // vector<int> v2;
    // v2.push_back(2);
    // v2.push_back(5);
    // v2.push_back(8);
    // v2.push_back(12);
    // v2.push_back(19);
    // matrix.push_back(v2);
    // vector<int> v3;
    // v3.push_back(3);
    // v3.push_back(6);
    // v3.push_back(9);
    // v3.push_back(16);
    // v3.push_back(22);
    // matrix.push_back(v3);
    // vector<int> v4;
    // v4.push_back(10);
    // v4.push_back(13);
    // v4.push_back(14);
    // v4.push_back(17);
    // v4.push_back(24);
    // matrix.push_back(v4);
    // vector<int> v5;
    // v5.push_back(18);
    // v5.push_back(21);
    // v5.push_back(23);
    // v5.push_back(26);
    // v5.push_back(30);
    // matrix.push_back(v5);

    if (sol.searchMatrix(matrix, 6)) {
        cout << "true" << endl;
    } else {
        cout << "false" << endl;
    }
    return 0;
}