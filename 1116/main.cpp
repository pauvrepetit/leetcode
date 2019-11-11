#include <functional>
#include <pthread.h>

using std::function;

class ZeroEvenOdd {
  private:
    int n;
    pthread_mutex_t mutex01;
    pthread_mutex_t mutex10;
    pthread_mutex_t mutex02;
    pthread_mutex_t mutex20;

  public:
    ZeroEvenOdd(int n) {
        this->n = n;
        pthread_mutex_init(&(this->mutex01), NULL);
        pthread_mutex_init(&(this->mutex10), NULL);
        pthread_mutex_init(&(this->mutex02), NULL);
        pthread_mutex_init(&(this->mutex20), NULL);
        pthread_mutex_lock(&(this->mutex01));
        pthread_mutex_lock(&(this->mutex10));
        pthread_mutex_lock(&(this->mutex02));
        // pthread_mutex_lock(&(this->mutex20));
    }

    // printNumber(x) outputs "x", where x is an integer.
    void zero(function<void(int)> printNumber) {
        int flag = 0;
        for (int i = 0; i < this->n; i++) {
            if (flag == 0) {
                pthread_mutex_lock(&(this->mutex20));
                printNumber(0);
                flag = 1;
                pthread_mutex_unlock(&(this->mutex01));
            } else {
                pthread_mutex_lock(&(this->mutex10));
                printNumber(0);
                flag = 0;
                pthread_mutex_unlock(&(this->mutex02));
            }
        }
    }

    void even(function<void(int)> printNumber) {
        for (int i = 2; i <= this->n; i += 2) {
            pthread_mutex_lock(&(this->mutex02));
            printNumber(i);
            pthread_mutex_unlock(&(this->mutex20));
        }
    }

    void odd(function<void(int)> printNumber) {
        for (int i = 1; i <= this->n; i += 2) {
            pthread_mutex_lock(&(this->mutex01));
            printNumber(i);
            pthread_mutex_unlock(&(this->mutex10));
        }
    }
};