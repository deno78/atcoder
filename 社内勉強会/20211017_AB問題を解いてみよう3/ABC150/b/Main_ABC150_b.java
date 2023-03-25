import java.util.*;

public class Main_ABC150_b {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n=Integer.valueOf(sc.next());
        String s=sc.next();
        int count=0;
        int next=0;
        while(next>-1){
            next=s.indexOf("ABC",next);
            if(next==-1){
                break;
            }
            next++;
            count++;
        }
        System.out.println(count);
    }
}