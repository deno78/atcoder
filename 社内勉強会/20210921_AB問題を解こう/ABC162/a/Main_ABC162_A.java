import java.util.*;

public class Main_ABC162_A {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
	String s =sc.next();
	// 受け取った文字列を単文字の配列としてアクセス
	for(char c : s.toCharArray()){
		if(c=='7'){
			// 1個でも条件を満たしたら回答して終了
			System.out.println("Yes");
			System.exit(0);
		}
	}
	// 全部外れならNo
	System.out.println("No");
    }
}
