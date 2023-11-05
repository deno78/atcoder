import java.util.*;

public class Main {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        if (n % 2 == 1) {
            System.out.println(1 + (n - 1) / 2);
            System.out.println(1);
            n -= 1;
        } else {
            System.out.println(n / 2);
        }
        for (int i = 0; i < n / 2; i++) {
            System.out.println(2);
        }
    }
}
