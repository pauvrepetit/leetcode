/* 409. 最长回文串
 * 
 * 20200907
 * huao
 */

#include <string.h>

int longestPalindrome(char * s){
    int count[128];
    memset(count, 0, sizeof(int) * 128);

    for (int i = 0; s[i] != 0; i++) {
        count[s[i]]++;
    }
    int flag = 0;
    int length = 0;
    for (int i = 'A'; i <= 'z'; i++) {
        if (count[i] % 2 == 1) {
            flag = 1;
            length += count[i] - 1;
        } else {
            length += count[i];
        }
    }
    return length + flag;
}