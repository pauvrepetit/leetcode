#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int movingCount(int m, int n, int k){
    char **reached = (char **)malloc(sizeof(char *) * m);
    for (int i = 0; i < m; i++) {
        reached[i] = (char *)malloc(sizeof(char) * n);
        memset(reached[i], 0, sizeof(char) * n);
    }
    reached[0][0] = 1;
    int count = 1;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (reached[i][j] == 1) continue;
            int can_reach = 0;
            if (i-1 >= 0 && j >= 0 && i-1 < m && j < n) can_reach += reached[i-1][j];
            if (i >= 0 && j-1 >= 0 && i < m && j-1 < n) can_reach += reached[i][j-1];
            if (i+1 >= 0 && j >= 0 && i+1 < m && j < n) can_reach += reached[i+1][j];
            if (i >= 0 && j+1 >= 0 && i < m && j+1 < n) can_reach += reached[i][j+1];
            int local_sum = i / 10 + i % 10 + j / 10 + j % 10;
            if (can_reach && local_sum <= k) {
                reached[i][j] = 1;
                count++;
            }
        }
    }
    return count;
}