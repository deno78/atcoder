import java.util.*;
public class Main_ABC159_b{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        String s1 = s.substring(0,(s.length()-1)/2);
        String s2 = s.substring((s.length()+3)/2-1);
        if(check(s) && check(s1) && check(s2)){
            System.out.println("Yes");
        }else{
            System.out.println("No");
        }
    }

    public static boolean check(String s){
        for(int i=0;i<s.length()/2;i++){
            int i2=s.length()-i-1;
            if(s.toCharArray()[i] != s.toCharArray()[i2]){
                return false;
            }
        }
        return true;
    }
}