/*
 * 3. 无重复字符的最长子串
 * 剑指 Offer 48. 最长不含重复字符的子字符串
 * 
 * huao
 */

#include <stdio.h>
#include <string.h>

int charinsubstring(char c, char* string, int begin, int len) {
    int i = 0;
    for (i = begin; i < begin + len; i++) {
        if (string[i] == c) {
            return 1;
        }
    }
    return 0;
}

int max(int a, int b) {
    if (a >= b) {
        return a;
    } else {
        return b;
    }
}

int lengthOfLongestSubstring(char* s) {
    int maxlen = 0;
    int i = 0, j = 0, flag = 0;
    int len = (int) strlen(s);
    if (len == 1) {
        return 1;
    }
    for (i = 0; i < len; i++) {
        flag = 0;
        for (j = i + 1; j < len; j++) {
            if (charinsubstring(s[j], s, i, j - i)) {
                maxlen = max(maxlen, j - i);
                flag = 1;
                break;
            }
        }
        if (flag == 0) {
            maxlen = max(maxlen, j - i);
        }
    }
    return maxlen;
}

int main() {
    char string[5] = "aab";
    printf("%d\n", lengthOfLongestSubstring(string));
    return 0;
}