import java.util.*;

public class Main_ABC141_b {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char[] s = sc.next().toCharArray();
        for (int i = 0; i < s.length; i++) {
            if (!check(i, s[i])) {
                System.out.println("No");
                System.exit(0);
            }
        }
        System.out.println("Yes");

    }

    public static boolean check(int i, char c1) {
        if (i % 2 == 0) {
            for (char c2 : new char[] { 'R', 'U', 'D' }) {
                if (c1 == c2) {
                    return true;
                }
            }
        } else {
            for (char c2 : new char[] { 'L', 'U', 'D' }) {
                if (c1 == c2) {
                    return true;
                }
            }
        }
        return false;

    }
}
