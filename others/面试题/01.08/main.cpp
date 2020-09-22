/*
 * 面试题 01.08. 零矩阵
 *
 * 20200920
 * Hu Ao
 */

#include <vector>

using namespace std;

class Solution {
public:
  void setZeroes(vector<vector<int>> &matrix) {
    int rowSize = matrix.size();
    int columnSize = matrix[0].size();
    int *rowZero = new int[rowSize];
    int *columnZero = new int[columnSize];
    memset(rowZero, 0, sizeof(int) * rowSize);
    memset(columnZero, 0, sizeof(int) * columnSize);
    for (int i = 0; i < rowSize; i++) {
      for (int j = 0; j < columnSize; j++) {
        if (matrix[i][j] == 0) {
          rowZero[i] = 1;
          columnZero[j] = 1;
        }
      }
    }

    for (int i = 0; i < rowSize; i++) {
      if (rowZero[i] == 1) {
        for (int j = 0; j < columnSize; j++) {
          matrix[i][j] = 0;
        }
      }
    }
    for (int i = 0; i < columnSize; i++) {
      if (columnZero[i] == 1) {
        for (int j = 0; j < rowSize; j++) {
          matrix[j][i] = 0;
        }
      }
    }
  }
};