import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int s = sc.nextInt();
        int t = sc.nextInt();
        int ans=0;
        int w=0;
        for(int i=0;i<n;i++){
            w+=sc.nextInt();
            if(s<=w && w<=t){
                ans+=1;
            }
        }
        System.out.println(ans);
    }
}