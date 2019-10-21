#include <iostream>
#include <pthread.h>

using std::cin;
using std::cout;
using std::endl;

class Foo {
public:
    pthread_t threadID[3];
    pthread_barrier_t barrier;

    Foo() {
        pthread_barrier_init(&barrier, NULL, 3);
    }

    void printFirst() {
        cout << "one";
    }
    void printSecond() {
        cout << "two";
    }
    void printThird() {
        cout << "three";
    }

    // void first(function<void()> printFirst) {
    void first() {
        threadID[0] = pthread_self();
        pthread_barrier_wait(&barrier);
        // printFirst() outputs "first". Do not change or remove this line.
        printFirst();
        pthread_exit(NULL);
    }

    // void second(function<void()> printSecond) {
    void second() {
        threadID[1] = pthread_self();
        pthread_barrier_wait(&barrier);
        pthread_join(threadID[0], NULL);
        // printSecond() outputs "second". Do not change or remove this line.
        printSecond();
        pthread_exit(NULL);
    }

    // void third(function<void()> printThird) {
    void third() {
        threadID[2] = pthread_self();
        pthread_barrier_wait(&barrier);
        pthread_join(threadID[1], NULL);
        // printThird() outputs "third". Do not change or remove this line.
        printThird();
        pthread_exit(NULL);
    }
};

int main(void)
{
    Foo foo;

    pthread_t thread[3];
    int temp;
    for (int i = 0; i < 3; i++)
    {
        cin >> temp;
        switch (temp)
        {
        case 1:
            pthread_create(&thread[i], NULL, foo.first, NULL);
            break;
        case 2:
            pthread_create(&thread[i], NULL, foo.second, NULL);
            break;
        case 3:
            pthread_create(&thread[i], NULL, foo.third, NULL);
            break;
        default:
            break;
        }
    }
    pthread_exit(NULL);
}