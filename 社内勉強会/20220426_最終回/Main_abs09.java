import java.util.*;

public class Main_abs09{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = Integer.valueOf(sc.next());
        int y = Integer.valueOf(sc.next());
        for(int i=0;i<(int)y/10000+1;i++){
            int m=y-i*10000;
            for(int j=0;j<(int)m/5000;j++){
                int k=n-i-j;
                if(i*10000+j*5000+k*1000==y){
                    System.out.println(i + " " + j + " " + k);
                    System.exit(0);
                }
            
            }
        }
        System.out.println("-1 -1 -1");        
    }
}