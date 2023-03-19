// 离谱的题目，还有离谱的leetcode判题器

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void my_strcpy(char *dst, char *src, int n) {
    for (int i = 0; i < n; i++) dst[i] = src[i];
}

void roll(char *s, int b, int n) {
    char *tmp = (char *)malloc(sizeof(char) * n);
    my_strcpy(tmp, s, n);
    for (int i = 0; i < n; i++) s[(i + b) % n] = tmp[i];
    free(tmp);
    return;
}

void add_odd(char *s, int a, int n) {
    for (int i = 1; i < n; i += 2) {
        s[i] += a;
        if (s[i] > '9') s[i] -= 10;
    }
    return;
}

void add_even(char *s, int a, int n) {
    for (int i = 0; i < n; i += 2) {
        s[i] += a;
        if (s[i] > '9') s[i] -= 10;
    }
    return;
}

char * findLexSmallestString(char * s, int a, int b){
    int n = 0;
    while (s[n] != 0) n++;
    char *tmp = (char *)malloc(sizeof(char) * (n+1));
    char *min = (char *)malloc(sizeof(char) * (n+1));
    min[n] = 0;
    tmp[n] = 0;
    my_strcpy(tmp, s, n);
    my_strcpy(min, s, n);
    if (b % 2 == 0) {
        // 当b是偶数时，只有奇数位可以累加，有10种可能
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < n; j++) {
                roll(tmp, b, n);
                if (strcmp(min, tmp) > 0) my_strcpy(min, tmp, n);
            }
            add_odd(tmp, a, n);
        }
    } else {
        for (int i = 0; i < 10; i++) {
            for (int k = 0; k < 10; k++) {
                for (int j = 0; j < n; j++) {
                    roll(tmp, b, n);
                    if (strcmp(min, tmp) > 0) my_strcpy(min, tmp, n);
                }
                add_even(tmp, a, n);
            }
            add_odd(tmp, a, n);
        }
    }
    free(tmp);
    return min;
    return s;
}

int main() {
    printf("%s\n", findLexSmallestString("5525", 9, 2));
    printf("%s\n", findLexSmallestString("74", 5, 1));
    printf("%s\n", findLexSmallestString("0011", 4, 2));
    printf("%s\n", findLexSmallestString("505648072863331802410297835524421704626903822492708213225203281871008551767440415344", 3, 49));
    return 0;
}
