/* 面试题 01.01. 判定字符是否唯一
 *
 * 20200726
 * huao
 * 
 * 还是C语言速度快，内存少
 * hahaha
 * 这个额外加上一个count[256]的结构来保存已经出现过的信息肯定是很好做的
 * 不过，如果不让额外使用内存空间的话，能不能实现呢？
 * 
 * 另，C语言貌似没有bool类型，true/false字面量
 */
#include <stdio.h>
#define TRUE 1
#define FALSE 0
typedef int bool;


bool isUnique(char* astr){
    int i = 0;
    char count[256] = {0};
    while(astr[i]) {
        if(count[astr[i]] != 0) {
            return FALSE;
        } else {
            count[astr[i]]++;
        }
    }
    return TRUE;
}

int main(void) {
    char *astr = "leetcode";
    if (isUnique(astr)) {
        printf("true");
    } else {
        printf("false");
    }
    return 0;
}