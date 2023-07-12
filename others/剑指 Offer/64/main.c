int sumNums(int n){
    int sum = n;
    (n != 0) && (sum += sumNums(n-1));
    return sum;
}