import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        String t = sc.next();
        int ans=0;
        for(int i=0;i<3;i++){
            if(s.charAt(i)==t.charAt(i)){
                ans++;
            }
        }
        System.out.println(ans);
    }    
}
