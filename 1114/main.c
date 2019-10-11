#include <stdlib.h>
#include <stdio.h>

void printFirst() {
    printf("first\n");
}

void printSecond() {
    printf("second\n");
}

void printThird() {
    printf("third\n");
}

typedef struct {
    volatile int first;
    volatile int second;
} Foo;

Foo* fooCreate() {
    Foo* obj = (Foo*) malloc(sizeof(Foo));
    obj->first = 0;
    obj->second = 0;
    return obj;
}

void first(Foo* obj) {
    printFirst();
    obj->first = 1;
}

void second(Foo* obj) {
    while(obj->first != 1);
    printSecond();
    obj->second = 1;
}

void third(Foo* obj) {
    while(obj->second != 1);
    printThird();
}

void fooFree(Foo* obj) {
    free(obj);    
}

// the main functon for test is fake
int main(void) {
    Foo * f = fooCreate();
    first(f);
    second(f);
    third(f);
    fooFree(f);
    return 0;
}
