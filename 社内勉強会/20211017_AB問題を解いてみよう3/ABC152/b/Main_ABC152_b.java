import java.util.*;

public class Main_ABC152_b {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a=Integer.valueOf(sc.next());
        int b=Integer.valueOf(sc.next());
        StringBuffer s1=new StringBuffer();
        StringBuffer s2=new StringBuffer();
        for(int i=0;i<b;i++){
            s1.append(Integer.toString(a));
        }
        for(int i=0;i<a;i++){
            s2.append(Integer.toString(b));
        }
        if(s1.compareTo(s2)<=0){
            System.out.println(s1);
        }else{
            System.out.println(s2);
        }
    }
}