package abc012_c;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.valueOf(sc.next());
	// 全部足した場合の合計値
        int all = 0;
	// 乗算結果と対応する式の連想配列
        Map<Integer, ArrayList<String>> map = new HashMap<Integer, ArrayList<String>>();
	// 1～9まで九九を計算
        for (int i = 1; i < 10; i++) {
            for (int j = 1; j < 10; j++) {
		// 合計を足していく
              	int a=i*j;
                all+=a;
		// 同時に連想配列に乗算結果と式を追加していく。
                Integer key = Integer.valueOf(a);
                if (!map.containsKey(key)) {
                    map.put(key, new ArrayList<String>());
                }
                map.get(key).add(String.format("%d x %d", i, j));
            }
        }
	// 忘れていた値の特定
        int d = Integer.valueOf(all - n);
	// 連想配列からリストを取り出して表示
        for (String s : map.get(d)) {
            System.out.println(s);
        }
    }

}
