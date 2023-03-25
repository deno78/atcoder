import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n=Integer.valueOf(sc.next());
        int t=Integer.valueOf(sc.next());
        int a=Integer.valueOf(sc.next());
        double min=Double.MAX_VALUE;
        int x=-1;
        for(int i=0;i<n;i++){
            int h=Integer.valueOf(sc.next());
            double p = Math.abs((t-h*0.006) - a);
            if(p<min){
                min=p;
                x=i;
            }
        }
        System.out.println(x+1);
    }
}
