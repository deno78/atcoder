import java.util.*;

public class Main2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.valueOf(sc.next());
        int m = Integer.valueOf(sc.next());
        // 引数をそのまま受け取るリスト
        List<Integer[]> pylist = new ArrayList<Integer[]>();

        // 年毎の市を記録していく連想配列
        Map<Integer, Integer> ymap = new HashMap<Integer, Integer>();
        for (int i = 0; i < m; i++) {
            int p = Integer.valueOf(sc.next());
            int y = Integer.valueOf(sc.next());
            ymap.put(y, p); // 各年にどの市の自治体が追加されたか、を記録
            Integer[] py = { p, y };
            pylist.add(py);
        }
        // 市毎のカウントアップするリストを作成
        int[] sequenses = new int[n+1];
        for (int i = 0; i <= n; i++) {
            sequenses[i] = 1;
        }

        // 年→認識番号を記録する連想配列
        Map<Integer, Integer> ydic = new HashMap<Integer, Integer>();

        // 年をソートしたリストを作成してループ
        List<Integer> ylist = new ArrayList<Integer>(ymap.keySet());
        Collections.sort(ylist);
        for (Integer y : ylist) {
            int p = ymap.get(y);
            int s = sequenses[p]; // どの市の件数か、を取得してループ
            sequenses[p]++;
            ydic.put(y, Integer.valueOf(s));
        }

        // 値＆順位の連想配列を調べながら表示していく
        for (Integer[] py : pylist) {
            Integer p = py[0];
            Integer y = py[1];
            System.out.println(String.format("%06d%06d", p, ydic.get(y)));
        }
    }
}
