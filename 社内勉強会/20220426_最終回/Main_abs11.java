import java.util.*;

public class Main_abs11{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n=Integer.valueOf(sc.next());
        int px=0;
        int py=0;
        int pt=0;
        for(int i=0;i<n;i++){
            int t=Integer.valueOf(sc.next());
            int x=Integer.valueOf(sc.next());
            int y=Integer.valueOf(sc.next());
            int d=Math.abs(px-x) + Math.abs(py-y);
            int wt=t-pt;
            if (wt<d){
                System.out.println("No");
                System.exit(0);
            }
            if ( (wt-d)%2>0 ){
                System.out.println("No");
                System.exit(0);
            }
            pt=t;
            px=x;
            py=y;            
        }
        System.out.println("Yes");
    }
}