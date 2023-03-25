import java.util.*;
public class Main_ABC139_b{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a=Integer.valueOf(sc.next());
        int b=Integer.valueOf(sc.next());
        int x=0;
        int t=1;
        while(t<b){
            x++;
            t+=(a-1);
        }
        System.out.println(x);
    }
}