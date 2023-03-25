import java.util.*;

public class Main1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.valueOf(sc.next());
        List<Integer> alist = new ArrayList<Integer>();
        for (int i = 0; i < n; i++) {
            int a = Integer.valueOf(sc.next());
            alist.add(a);
        }

        // 元リストを重複排除してソートしたリストを作る
        List<Integer> vlist = new ArrayList<Integer>(new HashSet<Integer>(alist));
        Collections.sort(vlist);

        // ソート済み＆重複排除したリストに順位を付けて値＆順位の連想配列に格納
        Map<Integer, Integer> amap = new HashMap<Integer, Integer>();
        for (int i = 0; i < vlist.size(); i++) {
            Integer v = (Integer) vlist.get(i);
            amap.put(v, i);
        }

        // 値＆順位の連想配列を調べながら表示していく
        for (Integer a : alist) {
            System.out.println(amap.get(a));
        }
    }
}
