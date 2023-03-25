import java.util.*;
public class Main_ABC139_a{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        char[] s=sc.next().toCharArray();
        char[] t=sc.next().toCharArray();
        int cnt=0;
        for(int i=0;i<3;i++){
            if(s[i]==t[i]){
                cnt++;
            }
        }
        System.out.println(cnt);
    }
}