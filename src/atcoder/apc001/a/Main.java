import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        if(x%y==0){
            System.out.println(-1);
        }else{
            int max = (int) Math.pow(10,19);
            int ans=-1;
            int i=1;
            while(true){
                int z=i++*x;
                if(z>max){break;}
                if(z%y!=0){
                    ans=z;
                    break;
                }
            }
            System.out.println(ans);
            }
    }
}