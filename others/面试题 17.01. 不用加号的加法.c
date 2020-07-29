/* 面试题 17.01. 不用加号的加法
 *
 * 20200729
 * huao
 * 看来我是把组原都忘干净了
 * 虽然我知道这东西在组原里面学过，可是并不知道要怎么去实现...
 */
#include <stdio.h>
struct SC {
    unsigned int s;
    int c;
};

struct SC addOne(unsigned int a, unsigned int b, int c) {
    unsigned int s = a ^ b ^ c;
    c = (c & (a ^ b)) | (a & b);
    struct SC result;
    result.s = s;
    result.c = c;
    return result;
}

struct SC add4(unsigned int a, unsigned int b, int c) {
    unsigned int s = 0;
    struct SC addOneResult = addOne(a & 1, b & 1, c);
    s |= addOneResult.s;

    a >>= 1;
    b >>= 1;
    addOneResult = addOne(a & 1, b & 1, addOneResult.c);
    s |= addOneResult.s << 1;

    a >>= 1;
    b >>= 1;
    addOneResult = addOne(a & 1, b & 1, addOneResult.c);
    s |= addOneResult.s << 2;

    a >>= 1;
    b >>= 1;
    addOneResult = addOne(a & 1, b & 1, addOneResult.c);
    s |= addOneResult.s << 3;

    addOneResult.s = s;
    return addOneResult;
}

struct SC add32(unsigned int a, unsigned int b, int c) {
    unsigned int s = 0;
    struct SC addOneResult = add4(a & 0xF, b & 0xF, c);
    s |= addOneResult.s;

    a >>= 4;
    b >>= 4;
    addOneResult = add4(a & 0xF, b & 0xF, addOneResult.c);
    s |= addOneResult.s << 4;

    a >>= 4;
    b >>= 4;
    addOneResult = add4(a & 0xF, b & 0xF, addOneResult.c);
    s |= addOneResult.s << 8;

    a >>= 4;
    b >>= 4;
    addOneResult = add4(a & 0xF, b & 0xF, addOneResult.c);
    s |= addOneResult.s << 12;

    a >>= 4;
    b >>= 4;
    addOneResult = add4(a & 0xF, b & 0xF, addOneResult.c);
    s |= addOneResult.s << 16;

    a >>= 4;
    b >>= 4;
    addOneResult = add4(a & 0xF, b & 0xF, addOneResult.c);
    s |= addOneResult.s << 20;

    a >>= 4;
    b >>= 4;
    addOneResult = add4(a & 0xF, b & 0xF, addOneResult.c);
    s |= addOneResult.s << 24;

    a >>= 4;
    b >>= 4;
    addOneResult = add4(a & 0xF, b & 0xF, addOneResult.c);
    s |= addOneResult.s << 28;

    addOneResult.s = s;
    return addOneResult;
}

int add(int a, int b) {
    return add32((unsigned)(a), (unsigned)(b), 0).s;
}

int main(void) {
    printf("%d\n", add(1, -2));
    // printf("10213 + 413214 = %d\n", add(-10213, 413214));
    // printf("10213 + 413214 = %d\n", add(10213, -413214));
    // printf("10213 + 413214 = %d\n", add(-10213, -413214));
    return 0;
}