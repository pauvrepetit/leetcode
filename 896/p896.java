/*
 * 896. 单调数列
 * 
 * 20200920
 * Hu Ao
 */

class Solution {
    public boolean isMonotonic(int[] A) {
        return this.isUpper(A) || this.isLower(A);
    }

    boolean isUpper(int[] A) {
        for (int i = 0; i < A.length - 1; i++) {
            if (A[i] > A[i + 1]) {
                return false;
            }
        }
        return true;
    }

    boolean isLower(int[] A) {
        for (int i = 0; i < A.length - 1; i++) {
            if (A[i] < A[i + 1]) {
                return false;
            }
        }
        return true;
    }
}

public class p896 {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] A = { 2, 2, 3, 4, 5 };
        System.out.println(sol.isMonotonic(A));
    }
}
