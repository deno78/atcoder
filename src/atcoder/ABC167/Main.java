import java.util.*;
class Main{
    public static void main(String[] a){
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        String t = sc.next();
        System.out.println(
            t.startsWith(s)&&s.length()==t.length()-1?"Yes":"No"
        );
    }
}