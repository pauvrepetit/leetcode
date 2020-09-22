/* 面试题 05.08. 绘制直线
 *
 * 20200802
 * huao
 * python的一些问题
 * python能够表示的数字范围很大，这导致在C/C++/Java中会溢出的操作在python中不会溢出
 * 所以结果是对的，但是表现出的效果不同
 */
#include <vector>

using std::vector;

class Solution {
  public:
    vector<int> drawLine(int length, int w, int x1, int x2, int y) {
        vector<int> screen;
        screen.resize(length);
        int width = w / 32;
        int height = length / width;
        for (int x = x1; x <= x2; x++) {
            screen[x / 32 + y * width] |= ((unsigned int)0x80000000 >> (x % 32));
        }
        return screen;
    }
};