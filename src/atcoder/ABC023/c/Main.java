import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int r = Integer.valueOf(sc.next());
        int c = Integer.valueOf(sc.next());
        int k = Integer.valueOf(sc.next());
        int n = Integer.valueOf(sc.next());
        List<Integer[]> rclist = new ArrayList<Integer[]>();
        // 注：合計件数はintに収まらない可能性がある...
        long[] rlist = new long[r];
        long[] clist = new long[c];
        // 縦横件数リストを0で初期化
        for (int i = 0; i < r; i++) {
            rlist[i] = 0;
        }
        for (int i = 0; i < c; i++) {
            clist[i] = 0;
        }

        // 入力値を受け取って、縦横件数とアメ位置に加算していく
        for (int i = 0; i < n; i++) {
            int x = Integer.valueOf(sc.next()) - 1;
            int y = Integer.valueOf(sc.next()) - 1;
            Integer[] xy = new Integer[] { x, y };
            rclist.add(xy);
            rlist[x] += 1;
            clist[y] += 1;
        }
        // 横位置のアメ数：件数のマップを作る
        Map<Long, Long> cmap = new HashMap<Long, Long>();
        for (int i = 0; i < clist.length; i++) {
            long cnt = clist[i];
            if (!cmap.containsKey(cnt)) {
                cmap.put(cnt, (long) 0);
            }
            long ccnt = cmap.get(cnt) + 1;
            cmap.put(cnt, ccnt);
        }
        // 縦位置を順番に舐めていく
        long sum = 0;
        for (long x : rlist) {
            if (cmap.containsKey(k - x)) {
                sum += cmap.get(k - x);
            }
        }
        // 各アメ位置について個別判定
        for (Integer[] xy : rclist) {
            int x = xy[0];
            int y = xy[1];
            long ame = rlist[x] + clist[y];
            if (ame == k) {
                // 合致なら重複して数えてしまっているので減算
                sum--;
            } else if (ame == k + 1) {
                // +1なら重複してちょうどになるので加算
                sum++;
            }
        }
        System.out.println(sum);
    }
}
