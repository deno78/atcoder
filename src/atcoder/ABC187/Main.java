import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String a=sc.next();
        String b=sc.next();
        System.out.println(
            Math.max(func(a),func(b))
        );
    }
    static int func(String s){
        int ret=0;
        for(int i=0;i<s.length();i++){
            ret+=(int) s.charAt(i)-48;
        }b
        return ret;
    }
    
}
