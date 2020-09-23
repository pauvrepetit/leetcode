/*
 * 829. 连续整数求和
 * 
 * 20200923
 * Hu Ao
 */

#include <cstdio>
#include <cmath>

class Solution {
public:
  int consecutiveNumbersSum(int N) {
    int count = 1;
    for (int i = 2; i <= sqrt(N) * 3 && i < N; i++) {
      if (i % 2 == 0) {
        if (N % i == i / 2 && N / i >= i / 2) {
          count += 1;
        }
      } else {
        if (N % i == 0 && N / i >= i / 2 + 1) {
          count += 1;
        }
      }
    }
    return count;
  }
};

int main(void) {
    Solution s = Solution();
    printf("%d\n", s.consecutiveNumbersSum(5));
    printf("%d\n", s.consecutiveNumbersSum(9));
    printf("%d\n", s.consecutiveNumbersSum(15));
    return 0;
}