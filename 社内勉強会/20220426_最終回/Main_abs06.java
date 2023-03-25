import java.util.*;

public class Main_abs06{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = Integer.valueOf(sc.next());
        int a = Integer.valueOf(sc.next());
        int b = Integer.valueOf(sc.next());

        int ans=0;
        for(int i=1;i<=n;i++){
            int x=0;
            String s = Integer.toString(i);
            for(int j=0;j<s.length();j++){
                x+=Integer.valueOf(s.substring(j,j+1));
            }
            if(a<=x && x<=b){
                ans+=i;
            }
        }
        System.out.println(ans);
    }
}