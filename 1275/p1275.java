/*
 * 1275. 找出井字棋的获胜者
 * 
 * 20200920
 * Hu Ao
 */

class Solution {
    public String tictactoe(int[][] moves) {
        int[][] chess = new int[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                chess[i][j] = -(i * 10 + j - 1);
            }
        }
        boolean role = true;
        for (int[] move : moves) {
            if (role) {
                chess[move[0]][move[1]] = 0;
            } else {
                chess[move[0]][move[1]] = 1;
            }
            if (this.check(chess)) {
                if (role) {
                    return "A";
                } else {
                    return "B";
                }
            }
            role = !role;
        }
        if (moves.length == 9) {
            return "Draw";
        } else {
            return "Pending";
        }
    }

    boolean check(int[][] chess) {
        for (int i = 0; i < 3; i++) {
            if (chess[i][0] == chess[i][1] && chess[i][1] == chess[i][2]) {
                return true;
            }
            if (chess[0][i] == chess[1][i] && chess[1][i] == chess[2][i]) {
                return true;
            }
        }
        if (chess[0][0] == chess[1][1] && chess[1][1] == chess[2][2]) {
            return true;
        }
        if (chess[0][2] == chess[1][1] && chess[1][1] == chess[2][0]) {
            return true;
        }
        return false;
    }
}

public class p1275 {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int moves[][] = { { 0, 2 }, { 1, 2 }, { 0, 1 }, { 1, 0 } };
        System.out.println(sol.tictactoe(moves));
    }
}
