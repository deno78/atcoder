import java.util.*;


public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int k = sc.nextInt();
        int s = sc.nextInt();
        int t = sc.nextInt();
        int ans = a*s+b*t;
        if(s+t>=k){
            ans-=c*(s+t);
        }
        System.out.println(ans);
    }
}
