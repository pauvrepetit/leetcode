/*
 * 面试题 01.02. 判定是否互为字符重排
 * 
 * 20200920
 * Hu Ao
 */

#include <string>

using namespace std;

class Solution {
public:
  bool CheckPermutation(string s1, string s2) {
    if (s1.length() != s2.length()) {
      return false;
    }
    int count1[260];
    int count2[260];
    memset(count1, 0, sizeof(int) * 260);
    memset(count2, 0, sizeof(int) * 260);

    for (auto &&c : s1) {
      count1[c] += 1;
    }
    for (auto &&c : s2) {
      count2[c] += 1;
    }
    for (int i = 0; i < 260; i++) {
      if (count1[i] != count2[i]) {
        return false;
      }
    }
    return true;
  }
};

int main(void) {
  Solution sol = Solution();
  if (sol.CheckPermutation("abc", "bcd")) {
    printf("True\n");
  } else {
    printf("False\n");
  }
  return 0;
}