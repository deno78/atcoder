import java.util.*;
public class Main_ABC140_b{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n=Integer.valueOf(sc.next());
        int[] alist=new int[n];
        int[] blist=new int[n];
        int[] clist=new int[n-1];
        for(int i=0;i<n;i++){
            alist[i]=Integer.valueOf(sc.next())-1;
        }
        for(int i=0;i<n;i++){
            blist[i]=Integer.valueOf(sc.next());
        }
        for(int i=0;i<n-1;i++){
            clist[i]=Integer.valueOf(sc.next());
        }
        int m=0; // 満足度
        int d=Integer.MIN_VALUE;
        for(int i=0;i<n;i++){
            int a=alist[i];
            m+=blist[a];
            if(d+1==a){
                    m+=clist[d];
                }
            d=a;
        }
        System.out.println(m);
    }
}