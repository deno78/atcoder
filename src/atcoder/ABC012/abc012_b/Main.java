package abc012_b;

import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = Integer.valueOf(sc.next());
	// 時を計算して元の秒数から引く
        int h=n/3600;
        n-=h*3600;
	// 分を計算して元の秒数から引く
        int m=n/60;
        n-=m*60;
	// 時、分、秒で表示。String.formatを使ってゼロ埋めする
        System.out.println(String.format("%02d:%02d:%02d",h,m,n));
    }
    
}
