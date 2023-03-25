import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 入力値を受け取る
        Scanner sc = new Scanner(System.in);
        int D = Integer.valueOf(sc.next());
        int[] C = new int[26];
        for (int i = 0; i < 26; i++) {
            C[i] = Integer.valueOf(sc.next());
        }
        int[][] S = new int[D][26];
        for (int i = 0; i < D; i++) {
            for (int j = 0; j < 26; j++) {
                S[i][j] = Integer.valueOf((sc.next()));
            }
        }
        int[] T =  new int[D];
        // 連番で振ってみる
        for(int d=0;d<D;d++){
            T[d]=d%26;            
        }
        // System.err.println(getScore(D,S,C,T));
        for(int t : T){
            System.out.println(t+1);
        }

    }

    public static int getScore(int D, int[][] S, int[] C, int[] T) {
        // 最後に開催した日の記録を作成して0で初期化
        int[] L = new int[26];
        for (int i = 0; i < D; i++) {
            L[i] = 0;
        }
        int m = 0; // 満足度
        for (int d = 0; d < D; d++) {
            int t = T[d];
            m += S[d][t];
            L[t] = d + 1;
            for (int i = 0; i < 26; i++) {
                m -= (d + 1 - L[i]) * C[i];
            }
        }
        return m;
    }

}