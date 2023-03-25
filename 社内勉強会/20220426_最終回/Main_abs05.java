import java.util.*;

public class Main_abs05{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a = Integer.valueOf(sc.next());
        int b = Integer.valueOf(sc.next());
        int c = Integer.valueOf(sc.next());
        int x = Integer.valueOf(sc.next());

        int ans=0;
        for(int i=0;i<a+1;i++){
            for(int j=0;j<b+1;j++){
                for(int k=0;k<c+1;k++){
                    if(i*500+j*100+k*50 == x){
                        ans++;
                    }
                }
            }
        }
        System.out.println(ans);
    }
}