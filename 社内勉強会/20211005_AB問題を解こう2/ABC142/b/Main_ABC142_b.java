import java.util.*;

public class Main_ABC142_b {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.valueOf(sc.next());
        int k = Integer.valueOf(sc.next());
        List<Integer> hlist = new ArrayList<Integer>();
        for (int i = 0; i < n; i++) {
            hlist.add(Integer.valueOf(sc.next()));
        }
        int ans = 0;
        for (int h : hlist) {
            if (h >= k) {
                ans++;
            }
        }
        System.out.println(ans);
    }
}
