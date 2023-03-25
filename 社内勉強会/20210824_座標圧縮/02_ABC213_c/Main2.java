import java.util.*;

public class Main2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int h = Integer.valueOf(sc.next());
        int w = Integer.valueOf(sc.next());
        int n = Integer.valueOf(sc.next());
        List<Integer> alist = new ArrayList<Integer>();
        List<Integer> blist = new ArrayList<Integer>();
        List<Integer[]> ablist = new ArrayList<Integer[]>();
        for (int i = 0; i < n; i++) {
            int a = Integer.valueOf(sc.next());
            int b = Integer.valueOf(sc.next());
            alist.add(a);
            blist.add(b);
            Integer[] ab = { a, b };
            ablist.add(ab);
        }

        // 元リストを重複排除してソートしたリストを作る
        List<Integer> valist = new ArrayList<Integer>(new HashSet<Integer>(alist));
        Collections.sort(valist);
        List<Integer> vblist = new ArrayList<Integer>(new HashSet<Integer>(blist));
        Collections.sort(vblist);

        // ソート済み＆重複排除したリストに順位を付けて値＆順位の連想配列に格納
        Map<Integer, Integer> amap = new HashMap<Integer, Integer>();
        Map<Integer, Integer> bmap = new HashMap<Integer, Integer>();
        for (int i = 0; i < valist.size(); i++) {
            Integer v = (Integer) valist.get(i);
            amap.put(v, i + 1);
        }
        for (int i = 0; i < vblist.size(); i++) {
            Integer v = (Integer) vblist.get(i);
            bmap.put(v, i + 1);
        }

        // 値＆順位の連想配列を調べながら表示していく
        for (Integer[] ab : ablist) {
            Integer a = ab[0];
            Integer b = ab[1];
            System.out.println(amap.get(a).toString() + " " + bmap.get(b).toString());
        }
    }
}
