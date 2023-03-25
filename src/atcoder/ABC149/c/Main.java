import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = Integer.valueOf(sc.next());

        // エラトステネスの篩　テンプレ
        int sz = 1000000;
        // 素数リストを初期化
        int[] plist = new int[sz];
        for (int i = 0; i < plist.length; i++) {
            plist[i] = i;
        }
        // 0,1は素数ではないので除外
        plist[0]=0;
        plist[1]=0;

        // 計算対象はサイズの平方根まで
        int last = (int) Math.sqrt(sz) + 1;
        // 2以上の数字について、倍数を消していく
        for (int i = 2; i <= last; i++) {
            if (plist[i] != 0) { // plist[i]が素数でなければ
                int sz2 = (int) sz / i ;
                // リスト上の倍数の部分を0に更新していく
                for (int j = 2; j < sz2; j++) {
                    plist[i*j] = 0;
                }
            }
        }

        // 最後にできた素数リストを1個づつ見ていく
        for (int p : plist) {
            if (p >= x) {
                System.out.println(p);
                System.exit(0);
            }
        }
    }
}
