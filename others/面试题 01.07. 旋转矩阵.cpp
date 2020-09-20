/*
 * 面试题 01.07. 旋转矩阵
 * 
 * 20200920
 * Hu Ao
 */

#include <vector>

using namespace std;

class Solution {
public:
  void rotate(vector<vector<int>> &matrix) {
    int matrixSize = matrix.size();
    for (int i = 0; i <= (matrixSize - 1) / 2; i++) {
      sol(matrix, i, matrixSize - i * 2);
    }
  }

  void sol(vector<vector<int>> &matrix, int level, int length) {
    int a = level;
    int b = level + length - 1;
    int t;
    for (int i = 0; i < b - a; i++) {
      t = matrix[a][a + i];
      matrix[a][a + i] = matrix[b - i][a];
      matrix[b - i][a] = matrix[b][b - i];
      matrix[b][b - i] = matrix[a + i][b];
      matrix[a + i][b] = t;
    }
  }
};

int main(void) {
  vector<vector<int>> matrix = {{1, 2, 3},
                                {4, 5, 6},
                                {7, 8, 9}};
  Solution sol = Solution();
  sol.rotate(matrix);
  return 0;
}