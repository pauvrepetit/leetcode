#include <stdio.h>

int hammingDistance(int x, int y) {
    int a = x ^ y;
    printf("%d\n", a);
    int i = 0, count = 0;
    for (i = 0; i < 32; ++i) {
        if ((1 << i) & a) {
            count++;
        }
    }
    return count;
}

int main() {
    printf("%d\n", hammingDistance(1, 4));
    return 0;
}