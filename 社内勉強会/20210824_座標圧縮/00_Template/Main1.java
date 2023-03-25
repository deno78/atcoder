import java.util.*;

public class Main1 {
    public static void main(String[] args) {
        List<Integer> alist = Arrays.asList(128,16,2,256,32,4,64,8);

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
            System.out.println(String.format("[%d] : %d",amap.get(a),a));
        }
    }
}
