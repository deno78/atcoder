import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.valueOf(sc.next());
        String s = sc.next();
        StringBuilder s2 = new StringBuilder("b");
        if (s.equals("b")) {
            System.out.println("0");
            System.exit(0);
        }
        int idx = 0;
        int cnt = 0;
        while (true) {
            idx++;
            cnt++;
            int t = idx % 3;
            if (t == 0) {
                s2.insert(0, "b");
                s2.append("b");
            } else if (t == 1) {
                s2.insert(0, "a");
                s2.append("c");
            } else if (t == 2) {
                s2.insert(0, "c");
                s2.append("a");
            }
            if (s.equals(s2.toString())) {
                System.out.println(cnt);
                System.exit(0);
            }
            if (s2.length() > n) {
                System.out.println("-1");
                System.exit(0);
            }
        }
    }
}
