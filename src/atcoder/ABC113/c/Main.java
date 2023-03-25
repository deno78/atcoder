import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.valueOf(sc.next());
        int m = Integer.valueOf(sc.next());

        // 入力値を引数順のリストと、県毎の連想配列に格納する
        List<int[]> pylist = new ArrayList<int[]>();
        Map<Integer, List<Integer>> pymap = new HashMap<Integer, List<Integer>>();
        for (int i = 0; i < m; i++) {
            int p = Integer.valueOf(sc.next());
            int y = Integer.valueOf(sc.next());
            pylist.add(new int[] { p, y });
            if (!pymap.containsKey(p)) {
                pymap.put(p, new ArrayList<Integer>());
            }
            pymap.get(p).add(y);
        }
        // 県毎にソートして認識番号を採番する
        Map<String, String> results = new HashMap<String, String>();
        for (Map.Entry<Integer, List<Integer>> pair : pymap.entrySet()) {
            int p = pair.getKey();
            List<Integer> ylist = pair.getValue();
            // 年順にソート
            Collections.sort(ylist);
            // 1から順に付番する
            for (int i = 1; i <= ylist.size(); i++) {
                // キーは仮に県＋年とする
                String key = String.format("%06d%06d", p, ylist.get(i - 1));
                String code = String.format("%06d%06d", p, i);
                results.put(key, code);
            }
        }
        // 入力リストと（県＋年）：認識番号の連想配列をぶつけて結果出力
        for (int[] py : pylist) {
            String key = String.format("%06d%06d", py[0], py[1]);
            System.out.println(results.get(key));
        }
    }

}
