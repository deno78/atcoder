import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 入力値受取
        Scanner sc = new Scanner(System.in);
        int h = Integer.valueOf(sc.next());
        int w = Integer.valueOf(sc.next());
        char[][] map = new char[h][w];
        for (int i = 0; i < h; i++) {
            String line = sc.next();
            for (int j = 0; j < line.length(); j++) {
                map[i][j] = line.charAt(j);
            }
        }
        // 今いるポジションを記録するキュー
        Queue<List<Integer>> pos = new ArrayDeque<List<Integer>>();

        // スタートから何手かかるか、を記録する歩数マップ。
        int[][] steps = new int[h][w];
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                steps[i][j] = -1;
                // 塗りつぶし開始位置を記録していく
                if(map[i][j]=='#'){
                    pos.add(Arrays.asList(i,j));
                    steps[i][j] = 0;
                }
            }
        }
        // 上下左右に動くパターンを先に作っておく
        List<int[]> moves = new ArrayList<int[]>();
        moves.add(new int[] { -1, 0 });
        moves.add(new int[] { 1, 0 });
        moves.add(new int[] { 0, -1 });
        moves.add(new int[] { 0, 1 });

        int ans=0;
        // 全部の場所を踏むまでループ
        while (pos.size() > 0) {
            // キューから1個取り出す
            List<Integer> yx = pos.remove();
            int y1 = yx.get(0);
            int x1 = yx.get(1);
            int step = steps[y1][x1];
            // その上下左右を調べる
            for (int[] m : moves) {
                int y2 = y1 + m[0];
                int x2 = x1 + m[1];
                // 座標を飛び出していないかチェック
                if (y2 >= 0 && x2 >= 0 && y2 < h && x2 < w) {
                    // 移動先が壁でなく、まだ歩数計測していない
                    if (map[y2][x2] == '.' && steps[y2][x2] == -1) {
                        // 1歩進める
                        steps[y2][x2] = step + 1;
                        ans=Math.max(step+1,ans);
                        // 次に調べるべき場所として記録しておく
                        pos.add(Arrays.asList(y2, x2));
                    }
                }
            }
            // for(int i=0;i<r;i++){
            // for(int j=0;j<c;j++){
            // System.out.print(String.format("[%d]", steps[i][j]));
            // }
            // System.out.println("");
            // }
            // System.out.println("----------------------------");
        }
        System.out.println(ans);
    }
}