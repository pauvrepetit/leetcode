#include <stdint.h>
#include <stdio.h>

int add(int a, int b){
    uint32_t ua = a;
    uint32_t ub = b;
    int res = 0;
    uint32_t mask = 1;
    int c = 0;
    while (ua != 0 || ub != 0) {
        uint32_t a_bit = ua & 1;
        uint32_t b_bit = ub & 1;
        uint32_t res_bit;
        if (a_bit && b_bit && c) {
            c = 1;
            res_bit = 1;
        } else if (a_bit && b_bit && !c) {
            c = 1;
            res_bit = 0;
        } else if (a_bit && !b_bit && c) {
            c = 1;
            res_bit = 0;
        } else if (a_bit && !b_bit && !c) {
            c = 0;
            res_bit = 1;
        } else if (!a_bit && b_bit && c) {
            c = 1;
            res_bit = 0;
        } else if (!a_bit && b_bit && !c) {
            c = 0;
            res_bit = 1;
        } else if (!a_bit && !b_bit && c) {
            c = 0;
            res_bit = 1;
        } else if (!a_bit && !b_bit && !c) {
            c = 0;
            res_bit = 0;
        }
        if (res_bit) {
            res |= (0xFFFFFFFF & mask);
        }
        mask <<= 1;
        ua >>= 1;
        ub >>= 1;
    }
    if (c) {
        res |= (0xFFFFFFFF & mask);
    }
    return res;
}

int main(void) {
    printf("%d\n", add(996614456, 893139330));
    return 0;
}