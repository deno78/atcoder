import java.util.*;

public class Main_abs10{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        for(String w : new String[]{"eraser","erase","dreamer","dream"}){
            s=s.replaceAll(w,"");
        }
        if(s.length()==0){
            System.out.println("YES");
        }else{
            System.out.println("NO");
        }
    }
}