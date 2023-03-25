import java.util.*;
public class Main_ABC139_b{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a=Integer.valueOf(sc.next());
        int b=Integer.valueOf(sc.next());
        int x=0;
        int t=1; // 全体口数
	// 全体の口数が目的の数を超えるまでループ
        while(t<b){
            x++; // タップを1個追加する
            t+=(a-1); // タップを1個追加すると口はa-1個増える
        }
        System.out.println(x);
    }
}
