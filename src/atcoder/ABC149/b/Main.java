import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a = Long.valueOf(sc.next());
        long b = Long.valueOf(sc.next());
        long k = Long.valueOf(sc.next());
        System.out
                .println(Long.toString(Math.max(0, a - k)) + " " + Long.toString(Math.max(0, b - Math.max(0, k - a))));
    }
}
