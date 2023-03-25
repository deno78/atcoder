import java.util.*;

public class Main_abs03{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int c=0;
        for(int i=0;i<3;i++){
            if(s.charAt(i)=='1'){
                c++;
            }
        }
        System.out.println(c);
    }
}