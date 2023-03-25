import java.util.*;

public class Main_ABC151_b {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n=Integer.valueOf(sc.next());
        int k=Integer.valueOf(sc.next());
        int m=Integer.valueOf(sc.next());
        int sum=0;
        for(int i=0;i<n-1;i++){
            sum+=Integer.valueOf(sc.next());
        }
        int x=m*n-sum;
        if(x<=k){
            System.out.println(Math.max(x,0));
        }else{
            System.out.println("-1");
        }
    }
}