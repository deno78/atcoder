import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int h = Integer.valueOf(sc.next());
        int w = Integer.valueOf(sc.next());

        // 入力値を受け取って数値二次元配列のマップを作る
        String[][] map = new String[h][w];
        for (int i = 0; i < h; i++) {
            String line = sc.next();
            for (int j = 0; j < w; j++) {
                map[i][j] = Character.toString(line.charAt(j));
            }
        }
        // 各マスについて調査
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                // 爆弾以外のマスであれば、周囲8マスを調べて件数をマップに反映
                if (!map[i][j].equals("#")) {
                    int count = 0;
                    for (int k = 0; k < 9; k++) {
                        int x = k % 3 - 1 + i;
                        int y = ((int) k / 3) - 1 + j;
                        // 調べる対象が範囲内(0-h/w)かつ爆弾だったらカウント
                        if (x >= 0 && y >= 0 && x < h && y < w && map[x][y].equals("#")) {
                            count++;
                        }
                    }
                    map[i][j] = Integer.toString(count);
                }
            }
        }
        // 全件表示していく
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                System.out.print(map[i][j]);
            }
            System.out.println("");
        }
    }
}
