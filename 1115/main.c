#include <pthread.h>

typedef struct {
    int n;
    pthread_mutex_t mutex12;
    pthread_mutex_t mutex23;
} FooBar;

FooBar* fooBarCreate(int n) {
    FooBar* obj = (FooBar*) malloc(sizeof(FooBar));
    obj->n = n;
    pthread_mutex_init(&(obj->mutex12), NULL);
    pthread_mutex_init(&(obj->mutex23), NULL);
    pthread_mutex_lock(&(obj->mutex12));
    // pthread_mutex_lock(&(obj->mutex23));
    return obj;
}

void foo(FooBar* obj) {
    for (int i = 0; i < obj->n; i++) {
        pthread_mutex_lock(&(obj->mutex23));
        printFoo();
        pthread_mutex_unlock(&(obj->mutex12));
    }
}

void bar(FooBar* obj) {
    for (int i = 0; i < obj->n; i++) {
        pthread_mutex_lock(&(obj->mutex12));
        printBar();
        pthread_mutex_unlock(&(obj->mutex23));
    }
}

void fooBarFree(FooBar* obj) {
    pthread_mutex_destroy(&(obj->mutex12));
    pthread_mutex_destroy(&(obj->mutex23));
    free(obj);
}