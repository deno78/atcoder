import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int v = sc.nextInt();
        int t = sc.nextInt();
        int s = sc.nextInt();
        int d = sc.nextInt();
        System.out.println(
            d<v*t||v*s<d?
            "Yes":"No"
        );
    }
    
}
